# MS Office Unprotector

> Inspect, disable, strip, and reset document protection from `.docx`, `.xlsx`, and `.pptx` files — no heavy dependencies, no hassle.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-lightgrey)
![Dependencies](https://img.shields.io/badge/Dependencies-stdlib%20only-brightgreen)

---

## Description

Modern Office Open XML files (`.docx`, `.xlsx`, `.pptx`) are just ZIP archives containing XML. When you apply document protection in Word, Excel, or PowerPoint, the app writes a handful of XML tags — `<w:documentProtection>`, `<workbookProtection>`, `<sheetProtection>`, `<p:modifyVerifier>` — into those XML files. That's it. There's no encryption; it's a restriction mechanism.

**MS Office Unprotector** is a clean, lightweight desktop tool that:

1. Unzips the Office file entirely in memory
2. Locates the relevant XML files and protection tags
3. Either **reports** what it finds, **disables** enforcement with a minimal attribute flip, **removes** the tags entirely, or **replaces** the password hash with an empty-password equivalent
4. Safely repacks the archive and writes it back to disk

Built as a single self-contained Python script using nothing but the standard library.

---

## Features

- **Clean architecture** — The core engine (`OfficeRuleModifier`) is a pure-Python class with zero UI imports. The Tkinter GUI (`OfficeModifierApp`) is a separate class wired on top. Logic and presentation never mix.
- **Zero external dependencies** — Powered entirely by `zipfile`, `xml.etree.ElementTree`, `tkinter`, `threading`, and `queue` — all stdlib. No `pip install` required.
- **Non-blocking UI** — Processing runs in a daemon background thread. A `queue.Queue` bridges the thread to the GUI, and `root.after(100, poll)` drains it on the main loop — the interface stays perfectly responsive during heavy batch jobs.
- **Graceful cancellation** — A `threading.Event` lets you cancel a batch mid-run. The engine always finishes the file it's currently processing before stopping, so no file is ever left half-written.
- **Automatic backups** — Before touching any file, the engine creates `filename_backup.ext`. If that already exists, it increments (`_backup_2`, `_backup_3`, …). Your originals are always safe.
- **Four modes** — *Scan & Report* (read-only audit), *Disable Protection* (flip enforcement off with minimal XML changes), *Strip Protection* (remove tags entirely), or *Modify Hash* (replace with empty-password hash so the file opens without prompting).
- **Single file or whole directory** — Process one document or batch-scan an entire folder tree.
- **Namespace-safe XML** — Registers 30+ OOXML namespace prefixes before any parsing so `ElementTree` never invents `ns0:` prefixes that corrupt the file. Preserves `standalone="yes"` in the XML declaration.

---

## Project Structure

```
msoffice-unprotector/
└── msoffice_unprotector.py
```

Everything lives in one file, organized into four logical sections with clear separator comments:

```python
# ── Section 1: Imports & Constants ──────────────────────
#    OOXML namespace registry, Action enum,
#    ProtectionTarget dataclass, target configs per format

# ── Section 2: Core Engine ──────────────────────────────
#    class OfficeRuleModifier — pure logic, no UI imports

# ── Section 3: GUI Application ──────────────────────────
#    class OfficeModifierApp — Tkinter + threading + queue

# ── Section 4: Entry Point ──────────────────────────────
#    if __name__ == '__main__': launch GUI
```

This layout keeps distribution dead-simple (share one file, run anywhere) while maintaining a hard logical boundary between the engine and the UI. The `OfficeRuleModifier` class can be imported and used from scripts or tests independently of Tkinter.

---

## Prerequisites & Installation

**Requirements:**
- Python **3.10 or newer** (uses `X | Y` union type hints)
- Tkinter — bundled with the standard CPython installer on Windows and macOS. On Linux you may need:
  ```bash
  sudo apt install python3-tk   # Debian/Ubuntu
  sudo dnf install python3-tkinter  # Fedora
  ```

**No `pip install` needed.** The tool uses only the Python standard library.

**Clone and run:**

```bash
git clone https://github.com/ZhunHao/msoffice-unprotector.git
cd msoffice-unprotector
python3 msoffice_unprotector.py
```

That's it. The GUI opens immediately.

---

## Usage

1. **Choose a Mode**
   - *Single File* — processes one `.docx`, `.xlsx`, or `.pptx` file
   - *Batch Processing* — scans an entire directory tree; use the file type checkboxes to filter

2. **Select your Target**
   Click **Browse...** to pick a file or folder.

3. **Pick an Action**

   | Action | What it does |
   |--------|-------------|
   | **Scan & Report Only** | Reads the file, finds protection elements, and logs their attributes. Nothing is modified. |
   | **Disable Protection** | The lightest touch: flips enforcement off with minimal attribute changes. For Word, sets `enforcement="0"`. For Excel, zeroes lock/permission attributes and removes hashes. For PowerPoint, removes the verifier element (no toggle exists). |
   | **Strip All Protection** | Removes protection XML elements entirely. The file opens with no restrictions. |
   | **Modify Password Hash** | Replaces the stored hash/salt with values computed for an empty password. Useful when Office prompts for a password on open. |

4. **Click Start**
   Watch the real-time log console. Progress is shown on the bar at the bottom. Click **Cancel** at any time to stop after the current file finishes.

5. **Check your backups**
   Before any modification, a backup is written next to the original:
   ```
   report.docx          ← modified in-place
   report_backup.docx   ← your original, untouched
   ```

---

## Disclaimer

This tool is intended **solely** for use on files you own or have explicit permission to modify — for example, recovering access to your own documents after forgetting a restriction password, or programmatically cleaning protection from files generated by your own workflows.

Document protection in Office Open XML is a **restriction mechanism, not encryption**. It is not a security boundary and was never designed to be one (Microsoft's own documentation acknowledges this). Bypassing it on documents you do not own may violate applicable laws or terms of service.

Use responsibly.

---

## License

MIT — see [LICENSE](LICENSE) for details.
