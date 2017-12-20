*** Settings ***
Library     Robot2nessus
Library     Collections


*** Variables ***

${SERVER_IP}    https://127.0.0.1:8834
${USERNAME}     admin
${PASSWORD}     pavan@123
${SSL}          False



${TARGET}       127.0.0.1,45.33.49.119
${PROJECT_NAME}     we45-automation
${POLICY}
${TEMPLATE}     basic



${SCAN_FOLDER_NAME}  ${PROJECT_NAME}
${SCAN_NAME}    robo-demo
${SCHEDULE_SCAN}


${REPORT_NAME}      ${SCAN_NAME}_nessus
@{FORMAT}=    html  nessus
${CATEGORY}    vuln_by_host
${DB_PASS}     we45@123


${HTML_SCAN_REPORT}     <a href=${REPORT_NAME}.html>HTML Format Report</a>
${XML_SCAN_REPORT}      <a href=${REPORT_NAME}.nessus>XML Format Report</a>



*** Test Cases ***
Nessus Scan
    [Documentation]  Nessus Automation
    [Tags]  Recon   Vulnerable assessment
    nessus login    ${SERVER_IP}    ${USERNAME}     ${PASSWORD}     ${SSL}
    set scan policy     ${POLICY}
    create scan  ${TARGET}  ${SCAN_FOLDER_NAME}     ${SCAN_NAME}    ${TEMPLATE}     ${SCHEDULE_SCAN}
    run scan
    scan results
    export scan results     ${REPORT_NAME}  ${FORMAT}   ${CATEGORY}     ${DB_PASS}
    log  ${HTML_SCAN_REPORT}   html=True
    log  ${XML_SCAN_REPORT}     html=True



