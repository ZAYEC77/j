# JCP — Jump Command for Projects

**JCP** is a small productivity tool that lets you define shell “projects” in YAML and instantly jump to them or run predefined commands from your terminal.

It generates Bash functions from YAML and loads them into your shell.

---

## What it does

* Jump to project directories
* Activate virtualenvs
* Start dev servers (npm, uvicorn, etc.)
* Run any shell commands
* Select projects interactively or by name

---

## How it works

```
jcp.yaml → get-jcp.py → jcp.sh → source in shell
```

1. Define projects in `jcp.yaml`
2. Run `get-jcp.py` to generate `jcp.sh`
3. Source `jcp.sh`
4. Use `j` or project names in your shell

---

## Installation

```bash
python3 ~/bin/get-jcp.py
source ~/bin/jcp.sh
```

Add to `~/.zshrc` or `~/.bashrc`:

```bash
source ~/bin/jcp.sh
```

---

## Usage

### Interactive selector

```bash
j
```

### Direct call

```bash
j backend
j frontend
```

or:

```bash
backend
```

---

## Configuration (`jcp.yaml`)

### Example: Python project with virtualenv

```yaml
projects:
  backend:
    directory: "~/projects/api"
    commands:
      - source .venv/bin/activate
      - export ENV=dev
      - echo "Backend ready"
```

---

### Example: Node.js project

```yaml
projects:
  frontend:
    directory: "~/projects/web"
    commands:
      - npm install
      - npm run dev
```

---

### Example: Utility project (no directory)

```yaml
projects:
  jcp-regen:
    commands:
      - python3 ~/bin/get-jcp.py
      - source ~/.zshrc
```

---

## Project fields

| Field       | Description                       |
| ----------- | --------------------------------- |
| `directory` | Directory to `cd` into (optional) |
| `commands`  | Shell commands to execute         |

---

## Regenerating

After editing `jcp.yaml`:

```bash
j jcp-regen
```

or:

```bash
python3 ~/bin/get-jcp.py
source ~/.zshrc
```

---

## Philosophy

* Simple code generation
* No magic
* Easy to debug
* Easy to extend and customize
* Shell-native behavior

If you can read Bash, you can understand what it generates.

---

## License

MIT (or whatever you prefer)
