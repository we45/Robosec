## Robot2Nessus

``Note: Required Field are marked as *``

***Nessus Login Configuration***

```
    ${SERVER_IP}    <*Nesus Running HOST>
    ${USERNAME}     <*Username>
    ${PASSWORD}     <*password>
    ${SSL}          True/False (Default: True)
```
***Scan Policy/Template Configuration***

```
    ${PROJECT_NAME} <*Project Name>
    ${POLICY}       <Not Required unless you have created your own policy configuration using Scan templates>
    ${TEMPLATE}     <*Required,Use InBuilt Nessus Template name>
```

***Scan Configuration***
```
    ${TARGET}            <*Single_IP> or <IP1,IP2,IP3>
    ${SCAN_FOLDER_NAME}  <Folder name to create scan on nessus> (Default Folder: My Scans)
    ${SCAN_NAME}         <*Scan Name>
    ${SCHEDULE_SCAN}     <YYYYMMDDTHHMMSS> (If require mention as YYYYMMDDTHHMMSS)
```

***Report  Configuration***
```
    ${REPORT_NAME}      ${SCAN_NAME} (Default: Same as Scan name)
    @{FORMAT}=          <*Report format>(html  nessus  db) i.e list of format
    ${CATEGORY}         <*Report Genration Method> (Required only for html & pdf format)
    ${DB_PASS}          <*db pass for database format) (Required for db format)

```

***InBuilt Nessus Scan Template List (Format-Title:Name)***

```
PCI Quarterly External Scan : asv
 Policy Compliance Auditing : compliance
 Audit Cloud Infrastructure : cloud_audit
  Internal PCI Network Scan : pci
  Bash Shellshock Detection : shellshock
   Credentialed Patch Audit : patch_audit
    GHOST (glibc) Detection : ghost
     SCAP and OVAL Auditing : scap
      web Application Tests : webapp
       Offline Config Audit : offline
         Basic Network Scan : basic
         Mobile Device Scan : mobile
          Badlock Detection : badlock
           MDM Config Audit : mdm
            DROWN Detection : drown
             Host Discovery : discovery
              Advanced Scan : advanced
               Malware Scan : malware
                Custom Scan : custom
```

***User Created Policy***

```
Nesus User Created Scan Policy Name List
    -Inte-PCI-scan-full
    -full_Advanced
    -advance_full_new
    -inte_PCI_complex
```

***Report Generation Category i.e ${CATEGORY}***
```
Required when exporting as HTML/PDF). Expecting a semi-colon delimited string comprised
of some combination of the following options:

                -vuln_hosts_summary,
                -vuln_by_host,
                -compliance_exec,
                -remediations,
                -vuln_by_plugin,
                -compliance.
```

### How to Run Robot2Nessus?

  1. Create a own policy template or choose any nessus scan templates as default for all Vulnerability Assessment.
  2. Then configure only project name and Scan Name each time for different Network VA.
  3. Run the Robot2Nessus.Robot using pybot with directory parameter to generate the report for both Robot Framework Test Suite and Nessus Scan.
  ```pybot -d results/ <script name>```

 **Note:Mention -d results/ while  running Robot2Nessus Script**





