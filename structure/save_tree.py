# structure/save_tree.py
import os
from pathlib import Path
from fnmatch import fnmatch


def load_gitignore_patterns(gitignore_path: str) -> list[str]:
    """
    Загружает шаблоны исключений из .gitignore
    """
    patterns = []
    with open(gitignore_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Убираем хвостовой слэш
            pattern = line.rstrip('/')

            # Преобразуем абсолютный путь (начинается с /) → относительный glob-путь
            if pattern.startswith('/'):
                pattern = pattern.lstrip('/')

            patterns.append(pattern)
    return patterns


def is_ignored(path: Path, patterns: list[str], project_root: Path) -> bool:
    """
    Проверяет, соответствует ли путь одному из паттернов в .gitignore
    """
    relative = path.relative_to(project_root)
    for pattern in patterns:
        if fnmatch(str(relative), pattern) or any(fnmatch(part, pattern) for part in relative.parts):
            return True
    return False


def save_tree(start_path: str, out_file: str, ignore_patterns: list[str]) -> None:
    """
    Рекурсивно сохраняет структуру проекта в файл, игнорируя файлы и папки из .gitignore.
    Папки отображаются перед файлами.
    """
    base_path = Path(start_path)
    with open(out_file, "w", encoding="utf-8") as f:
        for root, dirs, files in os.walk(base_path):
            root_path = Path(root)
            level = len(root_path.relative_to(base_path).parts)
            indent = '    ' * level

            if is_ignored(root_path, ignore_patterns, base_path):
                dirs[:] = []
                continue

            f.write(f"{indent}📁 {root_path.name}\n")

            # Сначала подкаталоги (не выводим отдельно — они попадут при следующем обходе)
            dirs[:] = [d for d in dirs if not is_ignored(root_path / d, ignore_patterns, base_path)]

            # Затем — файлы
            for file in sorted(files):
                file_path = root_path / file
                if is_ignored(file_path, ignore_patterns, base_path):
                    continue
                f.write(f"{indent}    📄 {file}\n")


if __name__ == "__main__":
    here = Path(__file__).resolve().parent
    root = here.parent
    gitignore = root / ".gitignore"
    patterns = load_gitignore_patterns(str(gitignore)) if gitignore.exists() else []

    save_tree(str(root), str(here / "project_structure.txt"), patterns)
