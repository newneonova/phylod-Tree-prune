# ===========================================================================
#
# Author:      Tony (http://MSHForFun.blogspot.com)
# File:        Efetch.ps1
# Description: Download gene sequences using NCBI eUtils.eFetch tool
# Reference: http://eutils.ncbi.nlm.nih.gov/entrez/query/static/eutils_example.pl
# Reference: http://eutils.ncbi.nlm.nih.gov/entrez/query/static/efetch_help.html
# Reference: http://eutils.ncbi.nlm.nih.gov/entrez/query/static/efetchseq_help.html
#  
# ===========================================================================
param
(
  [string] $Path=$(throw "Please Specify a file")
)
$BaseURL = "http://www.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nucleotide&id="
$Option= "&rettype=gp&retmode=text"
$WebClient = new-object System.Net.WebClient
$SavePath = $Path + ".result"
if (test-path $savePath)
{
  del $SavePath
}
foreach ( $id in (get-content $path))
{
  # Construct eFetch URL
  $URL=$BaseURL + $id + $Option
  Write-Progress -Activity "Download Taxonomy" -Status "Submit gene $Id"
  # Submit and download data
  $Data = $WebClient.DownloadString($URL)
  # Parse Data
  if ($Data.Length -gt 1)
  {
    Write-Progress -Activity "Download Sequences" -Status "$id OK"
    # Write to Console
	$dataO = $data -split "ORGANISM"
	$dataO =$dataO[1]
	$data1 = $dataO -split "REFERENCE"
	$data1 = $data1[0] 
    $data1
    # Wrtie To file
    $data1 >> $SavePath
  }
  else
  {
    Write-Progress -Activity "Download Sequences" -Status "$Id is not found!" 
    "$Id is not found!`n`r"
    "$Id is not found!`n`r" >> $SavePath
  }
  # Try not to overload NCBI Server
  start-sleep 1
}
# Clear Progress pane
Write-Progress -Activity "Download Sequences" -Status "Done" -completed 