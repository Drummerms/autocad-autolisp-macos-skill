# AutoLISP Function Compatibility Reference

Complete reference for AutoLISP function compatibility with AutoCAD for Mac.

## Compatibility Categories

| Category | Status | Description |
|----------|--------|-------------|
| Full | ✅ | Works on Mac with full functionality |
| Partial | ⚠️ | Works on Mac with limitations |
| Windows Only | ❌ | Does not work on Mac |

## Core AutoLISP Functions

### Command Execution (All Mac Compatible)

| Function | Mac | Description |
|----------|-----|-------------|
| `command` | ✅ | Execute AutoCAD commands |
| `command-s` | ✅ | Synchronous command execution |
| `vl-cmdf` | ✅ | Verified command execution |
| `initdia` | ✅ | Force dialog display |
| `initget` | ✅ | Set input options |

### Entity Functions (All Mac Compatible)

| Function | Mac | Description |
|----------|-----|-------------|
| `entmake` | ✅ | Create new entity |
| `entmakeX` | ✅ | Create extended entity |
| `entget` | ✅ | Get entity data |
| `entmod` | ✅ | Modify entity |
| `entdel` | ✅ | Delete entity |
| `entnext` | ✅ | Get next entity |
| `entsel` | ✅ | Select entity |
| `entupd` | ✅ | Update entity display |
| `handent` | ✅ | Get entity by handle |
| `nentsel` | ✅ | Nested entity selection |
| `nentselp` | ✅ | Nested entity selection with point |

### Selection Sets (All Mac Compatible)

| Function | Mac | Description |
|----------|-----|-------------|
| `ssget` | ✅ | Get selection set |
| `ssadd` | ✅ | Add to selection set |
| `ssdel` | ✅ | Delete from selection set |
| `sslength` | ✅ | Selection set length |
| `ssname` | ✅ | Entity name in set |
| `sssetfirst` | ✅ | Set grip selection |
| `ssgetfirst` | ✅ | Get grip selection |
| `ssmemb` | ✅ | Check membership |

### User Input Functions (All Mac Compatible)

| Function | Mac | Description |
|----------|-----|-------------|
| `getpoint` | ✅ | Get point |
| `getcorner` | ✅ | Get corner point |
| `getdist` | ✅ | Get distance |
| `getangle` | ✅ | Get angle |
| `getorient` | ✅ | Get orientation |
| `getint` | ✅ | Get integer |
| `getreal` | ✅ | Get real number |
| `getstring` | ✅ | Get string |
| `getkword` | ✅ | Get keyword |
| `getfiled` | ✅ | File dialog |
| `initget` | ✅ | Initialize input options |

### File Operations (All Mac Compatible)

| Function | Mac | Description |
|----------|-----|-------------|
| `open` | ✅ | Open file |
| `close` | ✅ | Close file |
| `read-line` | ✅ | Read line |
| `write-line` | ✅ | Write line |
| `read-char` | ✅ | Read character |
| `write-char` | ✅ | Write character |
| `findfile` | ✅ | Find file |
| `vl-file-list` | ✅ | List files |
| `vl-file-delete` | ✅ | Delete file |
| `vl-file-rename` | ✅ | Rename file |
| `vl-file-copy` | ✅ | Copy file |
| `vl-directory-files` | ✅ | List directory |

### Visual LISP Extensions (Most Mac Compatible)

| Function | Mac | Description |
|----------|-----|-------------|
| `vl-load-all` | ✅ | Load VL extensions |
| `vl-sort` | ✅ | Sort list |
| `vl-sort-i` | ✅ | Sort with indices |
| `vl-remove` | ✅ | Remove from list |
| `vl-remove-if` | ✅ | Remove if predicate |
| `vl-remove-if-not` | ✅ | Remove if not predicate |
| `vl-member-if` | ✅ | Member if predicate |
| `vl-position` | ✅ | Position in list |
| `vl-every` | ✅ | Every predicate |
| `vl-some` | ✅ | Some predicate |
| `vl-string-*` | ✅ | String functions |
| `vl-filename-*` | ✅ | Filename functions |
| `vl-propagate` | ✅ | Propagate to documents |
| `vl-symbol-*` | ✅ | Symbol functions |
| `vlax-*` | ❌ | ActiveX - Windows only |

## Windows-Only Functions

### ActiveX/COM Functions

All `vlax-*` functions are Windows only:

| Function | Alternative |
|----------|-------------|
| `vlax-get` | Use `entget` with DXF codes |
| `vlax-put` | Use `entmod` with modified data |
| `vlax-create-object` | Use `command` or external scripts |
| `vlax-get-acad-object` | Not available on Mac |
| `vlax-invoke-method` | Use `command` function |
| `vlax-dump-object` | Use `entget` |
| `vlax-ldata-*` | Use external config files |

### Reactor Functions

All `vlr-*` functions are Windows only:

| Function | Alternative |
|----------|-------------|
| `vlr-object-reactor` | Polling or command wrappers |
| `vlr-command-reactor` | Command wrappers or UNDO markers |
| `vlr-lisp-reactor` | Not available on Mac |
| `vlr-dwg-reactor` | Not available on Mac |
| `vl-load-reactors` | Not available on Mac |

### Express Tools

All `acet-*` functions are Windows only:

| Function | Alternative |
|----------|-------------|
| `acet-sys-wait` | Implement with `command` delay |
| `acet-str-replace` | Use `vl-string-subst` recursively |
| `acet-str-format` | Use `strcat` with formatting |
| `acet-ss-drag-*` | Implement custom drag |
| `acet-reg-*` | Use config files |
| `acet-file-*` | Use `vl-file-*` functions |

### Windows Registry

All `vl-registry-*` functions are Windows only:

| Function | Alternative |
|----------|-------------|
| `vl-registry-read` | Use JSON/LSP config files |
| `vl-registry-write` | Use JSON/LSP config files |
| `vl-registry-descendents` | Use external config |

### Windows-Only Dialogs

| Function | Alternative |
|----------|-------------|
| `acad_colordlg` | `(getint "Enter color: ")` |
| `acad_truecolordlg` | `(getint "Enter color: ")` |
| `acad_helpdlg` | Use `(help)` or external |

## Partial Support (Mac with Limitations)

### DCL Dialogs

DCL is supported on AutoCAD for Mac, but NOT on AutoCAD LT for Mac:

| Function | Mac | Notes |
|----------|-----|-------|
| `load_dialog` | ⚠️ | Works on full AutoCAD Mac only |
| `new_dialog` | ⚠️ | Works on full AutoCAD Mac only |
| `start_dialog` | ⚠️ | Works on full AutoCAD Mac only |
| `done_dialog` | ⚠️ | Works on full AutoCAD Mac only |
| `unload_dialog` | ⚠️ | Works on full AutoCAD Mac only |
| `action_tile` | ⚠️ | Works on full AutoCAD Mac only |
| `set_tile` | ⚠️ | Works on full AutoCAD Mac only |
| `get_tile` | ⚠️ | Works on full AutoCAD Mac only |
| `start_list` | ⚠️ | Works on full AutoCAD Mac only |
| `add_list` | ⚠️ | Works on full AutoCAD Mac only |
| `end_list` | ⚠️ | Works on full AutoCAD Mac only |

**DCL Limitations on Mac:**
- `allow_accept` attribute not supported for `edit_box` tile
- Uses more memory than on Windows
- Unload unused DCL definitions to conserve memory

## Quick Reference Patterns

### Pattern Matching for Compatibility

```python
# Windows-only prefixes
WINDOWS_ONLY_PREFIXES = ['vlax-', 'vlr-', 'acet-', 'vl-registry-']

# Check if function is likely Windows-only
def is_windows_only(func_name):
    return any(func_name.lower().startswith(prefix)
               for prefix in WINDOWS_ONLY_PREFIXES)
```

### Common Conversions

| Windows Pattern | Mac Pattern |
|-----------------|-------------|
| `(vlax-get obj 'Property)` | `(cdr (assoc 40 (entget obj)))` |
| `(vlax-put obj 'Property val)` | `(entmod (subst (cons 40 val) (assoc 40 (entget obj)) (entget obj)))` |
| `(vlax-create-object "App")` | Use `command` or shell out |
| `(vlr-object-reactor ...)` | Use polling or command hooks |
| `(acad_colordlg 1)` | `(getint "\nColor number: ")` |

## Using the Documentation

The `docs/` directory contains 4,500+ AutoCAD documentation files. To check a function:

```bash
grep -l "function-name-AutoLISP" docs/*.md
```

Look for the `*Supported Platforms:*` line in the result.
