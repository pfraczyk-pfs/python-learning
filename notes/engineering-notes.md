# Engineering Notes
## 2026-07-09

### Technical

#### pathlib

- `Path.home()` returns the current user's home directory.
- `Path.home() / "Downloads"` builds a platform-independent path.
- In `pathlib`, `/` joins paths instead of dividing numbers.

#### Directory traversal

- `iterdir()` iterates over every item in a directory.
- `is_file()` checks whether an item is a file.
- `name` returns the filename.
- `suffix` returns the file extension.

#### f-strings

- Prefixing a string with `f` allows embedding variables using `{}`.

---

### Engineering mindset

Today I realised that I don't need to memorize Python syntax.

I need to understand the problem first and then learn the syntax that solves it.

The workflow is more important than remembering individual functions.

---

### Reflection

The first working script gave me a feeling of control instead of fear.

I also realised that AI should explain my code before it writes my code.
## 2026-07-08

### Learned today

- GitHub Copilot is intentionally disabled during Sprint 1.
- AI should explain code, not write it for me.