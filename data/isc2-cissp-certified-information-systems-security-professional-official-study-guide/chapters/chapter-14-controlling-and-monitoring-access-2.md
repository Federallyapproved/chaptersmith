---
{
  "id": "chapter-276",
  "title": "Chapter 14: Controlling and Monitoring Access",
  "order": 276,
  "source": {
    "href": "b02.xhtml",
    "anchor": "head-2-37"
  },
  "est_tokens": 344,
  "slug": "chapter-14-controlling-and-monitoring-access-2",
  "meta": {
    "nav_title": "Chapter 14: Controlling and Monitoring Access",
    "enriched_from": "start-heading",
    "kind": "chapter"
  }
}
---
## Chapter 14: Controlling and Monitoring Access

- The primary difference between discretionary and nondiscretionary access control models is in how they are controlled and managed. Administrators centrally administer nondiscretionary access controls. DAC models allow owners to make their own changes, and their changes don't affect other parts of the environment.

- Some common standards used to provide SSO capabilities on the internet are Security Assertion Markup Language (SAML), OAuth, OpenID, and OpenID Connect (OIDC).

- The PowerShell cmdlet that allows you to run PowerShell commands indirectly is Invoke-Expression . The following command shows how to run it, assuming you have a PowerShell script named hello.ps1 in the current directory. powershell.exe "& {Get-Content .\hello.ps1 | Invoke-Expression} If you want to see this in action, create the hello.ps1 file with the following line: Write-Host 'Hello, World'

`Invoke-Expression`

`hello.ps1`

```

powershell.exe "& {Get-Content .\hello.ps1 | Invoke-Expression}
```

`powershell.exe "& {Get-Content .\hello.ps1 | Invoke-Expression}`

If you want to see this in action, create the hello.ps1 file with the following line:

`hello.ps1`

```

Write-Host 'Hello, World'
```

`Write-Host 'Hello, World'`

- Mimikatz is a popular tool used in privilege escalation attacks, including pass-the-hash and Kerberos exploitation attacks. PsExec, one of the tools in the Sysinternals process utilities (PsTools), is another tool often used in these attacks.
