## Robot2Burp

``Note: Required Field are marked as *``

***Burp Configuration***

```
    ${BURP_API_JAR_FILE}    <*Burp rest api jar file location>
    ${BURP_API_HOST}        <127.0.0.1 or External_IP> (Default:127.0.0.1)
    ${BURP_API_PROTOCOL}    <http or https> (Default:http)
    ${BURP_API_PORT}        <API service port> (Default:8090)
    ${JAVA_HOME}            <Java Home Folder> (Example: '/opt/jdk' not full location '/opt/jdk/bin/java')
    ${BURP_HEADLESS_MODE}   <true/false> (Default:True)
```

***Scan Configuration***

```
    ${SCOPE_URL}            <*Target Url>
    ${BURP_CONFIG}          <Burp Config file>
    ${REPORT_NAME}          <*Report Name>
    @{FORMAT}=              <*Report Format: HTML/XML>
```

***Report  Configuration***
```
   ${HTML_SCAN_REPORT}     <a href=${REPORT_NAME}.html>HTML Format Report</a>
   ${XML_SCAN_REPORT}      <a href=${REPORT_NAME}.xml>XML Format Report</a>
```


### How to Run Robot2Burp?
    
    1. Install the Burp Rest API (vmware) and generate Burp Rest API jar file from [burp-rest-api (vmware)](https://github.com/vmware/burp-rest-api)<br>
    2. Install the Burp Rest API Python Package.<br>
           ``Python setup.py install`` 
    3. Fill the configuration in the Robot2Burp.Robot script.
    3. Run the Robot2Burp.Robot using pybot with directory parameter to generate the report for both Robot Framework Test Suite and Nessus Scan.
    ```sudo pybot -d results/ <script name>```

   **Note:Mention -d results/ while  running Robot2Burp Script**





