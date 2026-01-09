#!/usr/bin/env python3

import argparse
import os
import yaml
import stat


def generate_shell_script(yaml_file: str, output_file: str):
    yaml_file = os.path.expanduser(yaml_file)
    output_file = os.path.expanduser(output_file)

    with open(yaml_file, "r") as f:
        config = yaml.safe_load(f)

    projects = config.get("projects", {})

    with open(output_file, "w") as f:
        # shebang
        f.write("#!/usr/bin/env bash\n")

        for project, details in projects.items():
            directory = details.get("directory")
            commands = details.get("commands", [])

            if directory:
                directory = os.path.expanduser(directory)

            # project function
            f.write(f"\n{project}() {{\n")
            if directory:
                f.write(f"  cd {directory} || return\n")
            for command in commands:
                f.write(f"  {command}\n")
            f.write("}\n")

        # j() selector
        f.write("\nj() {\n")
        f.write("    if [ $# -eq 1 ]; then\n")
        f.write("        choice=$1\n")
        f.write("    else\n")
        f.write("        echo 'Select a project:'\n")

        for idx, project in enumerate(projects):
            f.write(f"        echo '{idx}. {project}'\n")

        f.write("        read -r choice\n")
        f.write("    fi\n")
        f.write("    clear\n")
        f.write("    case $choice in\n")

        for idx, project in enumerate(projects):
            f.write(f"      {idx}) {project} ;;\n")

        for project in projects:
            f.write(f"      {project}) {project} ;;\n")

        f.write("      *) echo 'Invalid selection' ;;\n")
        f.write("    esac\n")
        f.write("}\n")

    # make executable
    st = os.stat(output_file)
    os.chmod(output_file, st.st_mode | stat.S_IEXEC)


def main():
    parser = argparse.ArgumentParser(
        description="Generate project jump shell functions from YAML"
    )
    parser.add_argument(
        "-i",
        "--input",
        default="~/bin/jcp.yaml",
        help="Path to YAML config (default: ~/bin/jcp.yaml)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="~/bin/jcp.sh",
        help="Path to output shell script (default: ~/bin/jcp.sh)",
    )

    args = parser.parse_args()

    generate_shell_script(args.input, args.output)

    print(f"Shell script generated: {os.path.expanduser(args.output)}")
    full_path = os.path.abspath(os.path.expanduser(args.output))
    print(f"Add this line to your ~/.zshrc or ~/.bashrc:\n```\n  source {full_path}\n```")
    

if __name__ == "__main__":
    main()
