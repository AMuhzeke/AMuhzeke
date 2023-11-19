$TZone = (Get-WMIObject -Class Win32_TimeZone).Bias
If ($TZone -eq 720)
  {
  Write-Host "You are on the opposite side of the world from Greenwich"
  }
  ElseIf ($TZone.Bias -gt 0)
  {
  Write-Host "You are currently east of Greenwich"
  }
  ElseIf ($TZone.Bias -lt 0)
  {
  Write-Host "You are currently west of Greenwich"
  }
  Else
  {
  Write-Host "You must be in Greenwich"
  }