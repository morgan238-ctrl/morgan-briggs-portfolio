# Adapted example of the application's read-only Access export pattern.
# Requires Windows and DAO.DBEngine.120. Syntax checked; Access execution untested.
# Example: supply a disposable Access file and an explicit table allowlist.
param(
    [Parameter(Mandatory=$true)][string]$Source,
    [Parameter(Mandatory=$true)][string]$Destination,
    [Parameter(Mandatory=$true)][string[]]$Tables
)
$ErrorActionPreference = 'Stop'
$sourcePath = [IO.Path]::GetFullPath($Source)
$destinationPath = [IO.Path]::GetFullPath($Destination)
if ([IO.Path]::GetExtension($sourcePath) -ne '.accdb' -or
    [IO.Path]::GetExtension($destinationPath) -ne '.json' -or
    $sourcePath -eq $destinationPath) { throw 'Choose separate Access and JSON paths.' }
foreach ($name in $Tables) {
    if ($name -notmatch '^[A-Za-z_][A-Za-z0-9_]*$') { throw 'Unsupported example table name.' }
}
$before = (Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash
$engine = New-Object -ComObject DAO.DBEngine.120
$database = $engine.OpenDatabase($sourcePath, $false, $true) # Read-only flag.
$output = [ordered]@{sourceSHA256=$before; tables=[ordered]@{}}
try {
    foreach ($name in $Tables) {
        $records = $database.OpenRecordset(('SELECT * FROM [' + $name + ']'), 4)
        $rows = [Collections.Generic.List[object]]::new()
        try {
            while (-not $records.EOF) {
                $row = [ordered]@{}
                foreach ($field in $records.Fields) {
                    $value = $field.Value
                    if ($value -is [DBNull]) { $value = $null }
                    if ($value -is [datetime]) { $value = $value.ToString('o') }
                    $row[$field.Name] = $value
                }
                $rows.Add($row)
                $records.MoveNext()
            }
        } finally { $records.Close() }
        $output.tables[$name] = @($rows.ToArray())
    }
} finally { $database.Close() }
if ((Get-FileHash -LiteralPath $sourcePath -Algorithm SHA256).Hash -ne $before) {
    throw 'Source changed during read; export rejected.'
}
$output | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $destinationPath -Encoding UTF8
