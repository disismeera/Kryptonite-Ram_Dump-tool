$output = @()

function PerformCommand {
    param (
        [scriptblock] $command,
        [string] $title
    )
    
    Write-Output $title | Out-File -Append -FilePath "Test.txt"
    Write-Output "==========================" | Out-File -Append -FilePath "Test.txt"
    $output = Invoke-Command $command
    $output | Out-File -Append -FilePath "Test.txt"
    Write-Output "" | Out-File -Append -FilePath "Test.txt"
}

PerformCommand { ipconfig /all } "IP Check"
PerformCommand { systeminfo } "System Info"

$wmiCommands = @(
    { Get-WmiObject Win32_Processor | Select-Object Name, Manufacturer, MaxClockSpeed, NumberOfCores },
    { Get-WmiObject Win32_VideoController | Select-Object Name, AdapterCompatibility, DriverVersion },
    { Get-WmiObject Win32_OperatingSystem | Select-Object Name, Caption, OSArchitecture, InstallDate, SerialNumber },
    { Get-WmiObject Win32_Product | Select-Object Name, Version, Vendor, InstallDate },
    { Get-WmiObject Win32_PerfFormattedData_PerfOS_Memory | Select-Object CommittedBytes, FreeAndZeroPageListBytes, CacheBytes, PoolPagedBytes, PoolNonpagedBytes },
    { Get-WmiObject Win32_PerfFormattedData_PerfOS_Processor | Select-Object Name, PercentProcessorTime },
    { Get-WmiObject Win32_PerfFormattedData_PerfDisk_PhysicalDisk | Select-Object Name, AvgDiskQueueLength, PercentDiskTime },
    { Get-WmiObject Win32_PerfFormattedData_Tcpip_NetworkInterface | Select-Object Name, BytesTotalPersec, BytesReceivedPersec, BytesSentPersec },
    { Get-WmiObject Win32_PerfFormattedData_PerfOS_System | Select-Object ProcessorQueueLength },
    { Get-WmiObject Win32_PerfFormattedData_PerfOS_PagingFile | Select-Object Name, PercentUsage },
    { Get-WmiObject SoftwareLicensingService | Select-Object OA3xOriginalProductKey }
)

foreach ($command in $wmiCommands) {
    PerformCommand $command.Invoke()
}

