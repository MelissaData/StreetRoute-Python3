# Name:    StreetRouteCloudAPI
# Purpose: Execute the StreetRouteCloudAPI program

######################### Parameters ##########################
param(
    $startlat = '', 
    $startlong = '', 
    $endlat = '', 
    $endlong = '', 
    $license = '', 
    [switch]$quiet = $false
    )

########################## Main ############################
Write-Host "`n======================== Melissa Street Route Cloud API ========================`n"

# Get license (either from parameters or user input)
if ([string]::IsNullOrEmpty($license) ) {
  $license = Read-Host "Please enter your license string"
}

# Check for License from Environment Variables 
if ([string]::IsNullOrEmpty($license) ) {
  $license = $env:MD_LICENSE 
}

if ([string]::IsNullOrEmpty($license)) {
  Write-Host "`nLicense String is invalid!"
  Exit
}

# Run project
if ([string]::IsNullOrEmpty($startlat) -and [string]::IsNullOrEmpty($startlong) -and [string]::IsNullOrEmpty($endlat) -and [string]::IsNullOrEmpty($endlong)) {

  python3 StreetRoutePython3.py --license $license 
}
else {
  python3 StreetRoutePython3.py --license $license --startlat $startlat --startlong $startlong --endlat $endlat --endlong $endlong 
}
