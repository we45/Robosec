*** Settings ***
Library     Robot2sublist3r


*** Variables ***
${PROJECT_NAME}         Robot_sublist3r-demo
${TARGET}               infogalactic.com
${THREAD_NO}            None
${OUTPUT_FILE_NAME}     ${PROJECT_NAME}-Sublist3r.txt
${PORT}                 None
${SILENT_MODE}          True
${VERBOSE}              False
${BRUTE_FORCE}          Flase
${ENGINES}              None



${NO_OUTPUT_MESSAGE}     No Subdomain have been identified, please use different scan option
${SUBLIST3R_SCAN_REPORT}      <a href=${OUTPUT_FILE_NAME}>Sublist3r Scan Report</a>




*** Test Cases ***
SubDomain Enumeration
    [Tags]  Recon   Subdomain Enumeration
    [Documentation]     Sublist3r Automation
    enumerate subdomain     ${TARGET}   ${THREAD_NO}  ${OUTPUT_FILE_NAME}   ${PORT}  ${SILENT_MODE} ${VERBOSE} ${BRUTE_FORCE} ${ENGINES}
    ${COUNT}=    get subdomain count
    ${MESSAGE}=    SET VARIABLE IF    '${COUNT}'=='0'  ${NO_OUTPUT_MESSAGE}     '${COUNT}'!= '0'    ${SUBLIST3R_SCAN_REPORT}
    LOG         <b>Scan Result</b><p>Subdomain Count: ${COUNT}</p>${MESSAGE}   html=True




