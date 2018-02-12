*** Settings ***
Library  Burp_api

*** Variables ***

${BURP_API_JAR_FILE}    ./burp-rest-api-1.0.0.jar
${BURP_API_HOST}        127.0.0.1
${BURP_API_PROTOCOL}    http
${BURP_API_PORT}        8090
${JAVA_HOME}            /home/pavan/Downloads/umar/jdk1.8.0_151
${BURP_HEADLESS_MODE}   true


${SCOPE_URL}            http://127.0.0.1:7777
${BURP_CONFIG}          ./democonfig.json
${REPORT_NAME}          demo_automation
@{FORMAT}=              HTML  XML


${HTML_SCAN_REPORT}     <a href=${REPORT_NAME}.html>HTML Format Report</a>
${XML_SCAN_REPORT}      <a href=${REPORT_NAME}.xml>XML Format Report</a>

${AUTH_TOKEN}       <Auth Token>
${WEBHOOK_URL}      <Orchestron Webhook Url>
${ENGAGEMENT_ID}    <optional leave blank if not neccessary>

*** Test Cases ***
Burp Automation:
    [Documentation]  Burp  Automation Via Burp Rest API
    [Tags]  Discovery   Exploitation
    start burp   ${BURP_API_JAR_FILE}    ${BURP_API_PROTOCOL}    ${BURP_API_HOST}    ${BURP_API_PORT}    ${BURP_HEADLESS_MODE}  ${JAVA_HOME}
    include scope  ${SCOPE_URL}
    check scope  ${SCOPE_URL}
    spider  ${SCOPE_URL}
    active scan  ${SCOPE_URL}
    scan status  ${SCOPE_URL}
    issue result  ${SCOPE_URL}
    generate report  ${SCOPE_URL}   ${REPORT_NAME}    ${FORMAT}
    stop burp
    orchy webhook   ${REPORT_NAME}  ${AUTH_TOKEN}   ${WEBHOOK_URL}  ${ENGAGEMENT_ID}
    log  ${HTML_SCAN_REPORT}   html=True
    log  ${XML_SCAN_REPORT}     html=True