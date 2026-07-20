# Vault Audit Procedure

Run `python project-code/scripts/audit_vault.py` from the vault root.

## Checks

- required root control files;
- Markdown and directory counts;
- empty or tiny notes;
- unresolved and ambiguous Obsidian links;
- duplicate filenames/stems;
- repeated placeholder boilerplate;
- Python syntax compilation;
- unit-test result;
- expected ZIP root name.

The generated report is stored in `output/VAULT_AUDIT.md`. A clean audit does not mean experiments are complete; it means the knowledge and starter implementation are internally consistent.
