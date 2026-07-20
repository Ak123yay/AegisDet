# Vault Audit Procedure

Run the workspace verifier from the workspace root:

```powershell
python verify_workspace.py
```

The verifier checks the required folder separation, confirms that `AegisDet Vault/project-code` does not exist, scans the vault for obsolete embedded-code references, checks required control files, and can run the code repository unit tests when dependencies are available.
