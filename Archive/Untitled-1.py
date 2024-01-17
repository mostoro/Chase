{
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 1104"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 1104"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },




{
  "Command": "comment",
  "Target": "CODE FOR ANOTHER ACCOUNT",
  "Value": "",
  "Description": ""
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page 2"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "click",
  "Target": "id=seeAllAccountsAG1Table",
  "Value": "",
  "Targets": [
    "id=seeAllAccountsAG1Table",
    "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
    "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
    "xpath=//mds-link",
    "css=#seeAllAccountsAG1Table"
  ],
  "Description": "Clicking \"See all accounts\""
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
  "Value": "",
  "Description": "Selecting bank account 3702"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Selecting bank account 3702"
},
{
  "Command": "click",
  "Target": "id=headerSearchLink",
  "Value": "",
  "Targets": [
    "id=headerSearchLink",
    "xpath=//*[@id=\"headerSearchLink\"]",
    "xpath=//mds-link[@id='headerSearchLink']",
    "xpath=//div[3]/mds-link",
    "css=#headerSearchLink"
  ],
  "Description": "Searching"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
  "Value": "",
  "Description": "Selecting from date"
},
{
  "Command": "XType",
  "Target": "${FromDate}",
  "Value": "",
  "Description": "Typing from date"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ",
  "Value": "",
  "Description": "Selecting to date"
},
{
  "Command": "XType",
  "Target": "${ToDate}",
  "Value": "",
  "Description": "Typing to date"
},
{
  "Command": "click",
  "Target": "id=activitySearchFilter",
  "Value": "",
  "Targets": [
    "id=activitySearchFilter",
    "xpath=//*[@id=\"activitySearchFilter\"]",
    "xpath=//mds-button[@id='activitySearchFilter']",
    "xpath=//div[2]/div[2]/mds-button",
    "css=#activitySearchFilter"
  ],
  "Description": "Clicking search after indicating dates"
},
{
  "Command": "pause",
  "Target": "2000",
  "Value": "",
  "Description": "Pausing to avoid issues"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "initialTitle",
  "Description": "Checking initialTitle"
},
{
  "Command": "echo",
  "Target": "The page title is ${initialTitle}\t",
  "Value": "",
  "Description": "Echo for initialTitle"
},
{
  "Command": "click",
  "Target": "id=downloadActivityIcon",
  "Value": "",
  "Targets": [
    "id=downloadActivityIcon",
    "xpath=//*[@id=\"downloadActivityIcon\"]",
    "xpath=//mds-button[@id='downloadActivityIcon']",
    "xpath=//span[2]/mds-button",
    "css=#downloadActivityIcon"
  ],
  "Description": "Clicking download buttom"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "afterClickTitle",
  "Description": "Checking afterClickTitle"
},
{
  "Command": "if",
  "Target": "${initialTitle} != ${afterClickTitle}",
  "Value": "",
  "Description": "Evaluating if download page is open"
},
{
  "Command": "echo",
  "Target": "New page opened.",
  "Value": "green",
  "Description": "Echo if new page opened"
},
{
  "Command": "click",
  "Target": "id=download",
  "Value": "",
  "Targets": [
    "id=download",
    "xpath=//*[@id=\"download\"]",
    "xpath=//mds-button[@id='download']",
    "xpath=//div[2]/mds-button",
    "css=#download"
  ],
  "Description": "Downloading report"
},
{
  "Command": "XType",
  "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "pause",
  "Target": "3000",
  "Value": "",
  "Description": "Pausing 3 secs to refresh after it"
},
{
  "Command": "else",
  "Target": "",
  "Value": "",
  "Description": "Actions if download page doesn´t exist"
},
{
  "Command": "echo",
  "Target": "No new page opened.",
  "Value": "red",
  "Description": "Echo for no new page opened"
},
{
  "Command": "click",
  "Target": "id=requestAccounts",
  "Value": "",
  "Targets": [
    "id=requestAccounts",
    "xpath=//*[@id=\"requestAccounts\"]",
    "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
    "xpath=//mds-navigation-bar-item",
    "css=#requestAccounts"
  ],
  "Description": "Returning to main page when there aren´t movements"
},
{
  "Command": "end",
  "Target": "",
  "Value": "",
  "Description": "Closing if condition"
},



  
    

{
  "Command": "comment",
  "Target": "CODE FOR ANOTHER ACCOUNT",
  "Value": "",
  "Description": ""
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page 2"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "click",
  "Target": "id=seeAllAccountsAG1Table",
  "Value": "",
  "Targets": [
    "id=seeAllAccountsAG1Table",
    "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
    "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
    "xpath=//mds-link",
    "css=#seeAllAccountsAG1Table"
  ],
  "Description": "Clicking \"See all accounts\""
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
  "Value": "",
  "Description": "Selecting bank account 1263"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Selecting bank account 1263"
},
{
  "Command": "click",
  "Target": "id=headerSearchLink",
  "Value": "",
  "Targets": [
    "id=headerSearchLink",
    "xpath=//*[@id=\"headerSearchLink\"]",
    "xpath=//mds-link[@id='headerSearchLink']",
    "xpath=//div[3]/mds-link",
    "css=#headerSearchLink"
  ],
  "Description": "Searching"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
  "Value": "",
  "Description": "Selecting from date"
},
{
  "Command": "XType",
  "Target": "${FromDate}",
  "Value": "",
  "Description": "Typing from date"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ",
  "Value": "",
  "Description": "Selecting to date"
},
{
  "Command": "XType",
  "Target": "${ToDate}",
  "Value": "",
  "Description": "Typing to date"
},
{
  "Command": "click",
  "Target": "id=activitySearchFilter",
  "Value": "",
  "Targets": [
    "id=activitySearchFilter",
    "xpath=//*[@id=\"activitySearchFilter\"]",
    "xpath=//mds-button[@id='activitySearchFilter']",
    "xpath=//div[2]/div[2]/mds-button",
    "css=#activitySearchFilter"
  ],
  "Description": "Clicking search after indicating dates"
},
{
  "Command": "pause",
  "Target": "2000",
  "Value": "",
  "Description": "Pausing to avoid issues"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "initialTitle",
  "Description": "Checking initialTitle"
},
{
  "Command": "echo",
  "Target": "The page title is ${initialTitle}\t",
  "Value": "",
  "Description": "Echo for initialTitle"
},
{
  "Command": "click",
  "Target": "id=downloadActivityIcon",
  "Value": "",
  "Targets": [
    "id=downloadActivityIcon",
    "xpath=//*[@id=\"downloadActivityIcon\"]",
    "xpath=//mds-button[@id='downloadActivityIcon']",
    "xpath=//span[2]/mds-button",
    "css=#downloadActivityIcon"
  ],
  "Description": "Clicking download buttom"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "afterClickTitle",
  "Description": "Checking afterClickTitle"
},
{
  "Command": "if",
  "Target": "${initialTitle} != ${afterClickTitle}",
  "Value": "",
  "Description": "Evaluating if download page is open"
},
{
  "Command": "echo",
  "Target": "New page opened.",
  "Value": "green",
  "Description": "Echo if new page opened"
},
{
  "Command": "click",
  "Target": "id=download",
  "Value": "",
  "Targets": [
    "id=download",
    "xpath=//*[@id=\"download\"]",
    "xpath=//mds-button[@id='download']",
    "xpath=//div[2]/mds-button",
    "css=#download"
  ],
  "Description": "Downloading report"
},
{
  "Command": "XType",
  "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "pause",
  "Target": "3000",
  "Value": "",
  "Description": "Pausing 3 secs to refresh after it"
},
{
  "Command": "else",
  "Target": "",
  "Value": "",
  "Description": "Actions if download page doesn´t exist"
},
{
  "Command": "echo",
  "Target": "No new page opened.",
  "Value": "red",
  "Description": "Echo for no new page opened"
},
{
  "Command": "click",
  "Target": "id=requestAccounts",
  "Value": "",
  "Targets": [
    "id=requestAccounts",
    "xpath=//*[@id=\"requestAccounts\"]",
    "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
    "xpath=//mds-navigation-bar-item",
    "css=#requestAccounts"
  ],
  "Description": "Returning to main page when there aren´t movements"
},
{
  "Command": "end",
  "Target": "",
  "Value": "",
  "Description": "Closing if condition"
},













    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 9306"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 9306"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },



    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 1012"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 1012"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },


{
  "Command": "comment",
  "Target": "CODE FOR ANOTHER ACCOUNT",
  "Value": "",
  "Description": ""
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page 2"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "click",
  "Target": "id=seeAllAccountsAG1Table",
  "Value": "",
  "Targets": [
    "id=seeAllAccountsAG1Table",
    "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
    "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
    "xpath=//mds-link",
    "css=#seeAllAccountsAG1Table"
  ],
  "Description": "Clicking \"See all accounts\""
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
  "Value": "",
  "Description": "Selecting bank account 6500"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Selecting bank account 6500"
},
{
  "Command": "click",
  "Target": "id=headerSearchLink",
  "Value": "",
  "Targets": [
    "id=headerSearchLink",
    "xpath=//*[@id=\"headerSearchLink\"]",
    "xpath=//mds-link[@id='headerSearchLink']",
    "xpath=//div[33702]/mds-link",
    "css=#headerSearchLink"
  ],
  "Description": "Searching"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
  "Value": "",
  "Description": "Selecting from date"
},
{
  "Command": "XType",
  "Target": "${FromDate}",
  "Value": "",
  "Description": "Typing from date"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ",
  "Value": "",
  "Description": "Selecting to date"
},
{
  "Command": "XType",
  "Target": "${ToDate}",
  "Value": "",
  "Description": "Typing to date"
},
{
  "Command": "click",
  "Target": "id=activitySearchFilter",
  "Value": "",
  "Targets": [
    "id=activitySearchFilter",
    "xpath=//*[@id=\"activitySearchFilter\"]",
    "xpath=//mds-button[@id='activitySearchFilter']",
    "xpath=//div[2]/div[2]/mds-button",
    "css=#activitySearchFilter"
  ],
  "Description": "Clicking search after indicating dates"
},
{
  "Command": "pause",
  "Target": "2000",
  "Value": "",
  "Description": "Pausing to avoid issues"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "initialTitle",
  "Description": "Checking initialTitle"
},
{
  "Command": "echo",
  "Target": "The page title is ${initialTitle}\t",
  "Value": "",
  "Description": "Echo for initialTitle"
},
{
  "Command": "click",
  "Target": "id=downloadActivityIcon",
  "Value": "",
  "Targets": [
    "id=downloadActivityIcon",
    "xpath=//*[@id=\"downloadActivityIcon\"]",
    "xpath=//mds-button[@id='downloadActivityIcon']",
    "xpath=//span[2]/mds-button",
    "css=#downloadActivityIcon"
  ],
  "Description": "Clicking download buttom"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "afterClickTitle",
  "Description": "Checking afterClickTitle"
},
{
  "Command": "if",
  "Target": "${initialTitle} != ${afterClickTitle}",
  "Value": "",
  "Description": "Evaluating if download page is open"
},
{
  "Command": "echo",
  "Target": "New page opened.",
  "Value": "green",
  "Description": "Echo if new page opened"
},
{
  "Command": "click",
  "Target": "id=download",
  "Value": "",
  "Targets": [
    "id=download",
    "xpath=//*[@id=\"download\"]",
    "xpath=//mds-button[@id='download']",
    "xpath=//div[2]/mds-button",
    "css=#download"
  ],
  "Description": "Downloading report"
},
{
  "Command": "XType",
  "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "pause",
  "Target": "3000",
  "Value": "",
  "Description": "Pausing 3 secs to refresh after it"
},
{
  "Command": "else",
  "Target": "",
  "Value": "",
  "Description": "Actions if download page doesn´t exist"
},
{
  "Command": "echo",
  "Target": "No new page opened.",
  "Value": "red",
  "Description": "Echo for no new page opened"
},
{
  "Command": "click",
  "Target": "id=requestAccounts",
  "Value": "",
  "Targets": [
    "id=requestAccounts",
    "xpath=//*[@id=\"requestAccounts\"]",
    "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
    "xpath=//mds-navigation-bar-item",
    "css=#requestAccounts"
  ],
  "Description": "Returning to main page when there aren´t movements"
},
{
  "Command": "end",
  "Target": "",
  "Value": "",
  "Description": "Closing if condition"
},
{
  "Command": "comment",
  "Target": "CODE FOR ANOTHER ACCOUNT",
  "Value": "",
  "Description": ""
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "XType",
  "Target": "${KEY_F5}",
  "Value": "",
  "Description": "Refreshing the web page 2"
},
{
  "Command": "pause",
  "Target": "3500",
  "Value": "",
  "Description": "Pausing to refresh again and avoid issues"
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "click",
  "Target": "id=seeAllAccountsAG1Table",
  "Value": "",
  "Targets": [
    "id=seeAllAccountsAG1Table",
    "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
    "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
    "xpath=//mds-link",
    "css=#seeAllAccountsAG1Table"
  ],
  "Description": "Clicking \"See all accounts\""
},
{
  "Command": "bringBrowserToForeground",
  "Target": "",
  "Value": "",
  "Description": "This is to update the focus on Chase web page (it is useful for tab)"
},
{
  "Command": "click",
  "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
  "Value": "",
  "Targets": [
    "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
    "xpath=//div[6]/div/div/div/div[2]",
    "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
  ],
  "Description": "Clicking to focus the page"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
  "Value": "",
  "Description": "Selecting bank account 0662"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Selecting bank account 0662"
},
{
  "Command": "click",
  "Target": "id=headerSearchLink",
  "Value": "",
  "Targets": [
    "id=headerSearchLink",
    "xpath=//*[@id=\"headerSearchLink\"]",
    "xpath=//mds-link[@id='headerSearchLink']",
    "xpath=//div[3]/mds-link",
    "css=#headerSearchLink"
  ],
  "Description": "Searching"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
  "Value": "",
  "Description": "Selecting from date"
},
{
  "Command": "XType",
  "Target": "${FromDate}",
  "Value": "",
  "Description": "Typing from date"
},
{
  "Command": "XType",
  "Target": "${KEY_TAB} ${KEY_TAB} ",
  "Value": "",
  "Description": "Selecting to date"
},
{
  "Command": "XType",
  "Target": "${ToDate}",
  "Value": "",
  "Description": "Typing to date"
},
{
  "Command": "click",
  "Target": "id=activitySearchFilter",
  "Value": "",
  "Targets": [
    "id=activitySearchFilter",
    "xpath=//*[@id=\"activitySearchFilter\"]",
    "xpath=//mds-button[@id='activitySearchFilter']",
    "xpath=//div[2]/div[2]/mds-button",
    "css=#activitySearchFilter"
  ],
  "Description": "Clicking search after indicating dates"
},
{
  "Command": "pause",
  "Target": "2000",
  "Value": "",
  "Description": "Pausing to avoid issues"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "initialTitle",
  "Description": "Checking initialTitle"
},
{
  "Command": "echo",
  "Target": "The page title is ${initialTitle}\t",
  "Value": "",
  "Description": "Echo for initialTitle"
},
{
  "Command": "click",
  "Target": "id=downloadActivityIcon",
  "Value": "",
  "Targets": [
    "id=downloadActivityIcon",
    "xpath=//*[@id=\"downloadActivityIcon\"]",
    "xpath=//mds-button[@id='downloadActivityIcon']",
    "xpath=//span[2]/mds-button",
    "css=#downloadActivityIcon"
  ],
  "Description": "Clicking download buttom"
},
{
  "Command": "storeTitle",
  "Target": "",
  "Value": "afterClickTitle",
  "Description": "Checking afterClickTitle"
},
{
  "Command": "if",
  "Target": "${initialTitle} != ${afterClickTitle}",
  "Value": "",
  "Description": "Evaluating if download page is open"
},
{
  "Command": "echo",
  "Target": "New page opened.",
  "Value": "green",
  "Description": "Echo if new page opened"
},
{
  "Command": "click",
  "Target": "id=download",
  "Value": "",
  "Targets": [
    "id=download",
    "xpath=//*[@id=\"download\"]",
    "xpath=//mds-button[@id='download']",
    "xpath=//div[2]/mds-button",
    "css=#download"
  ],
  "Description": "Downloading report"
},
{
  "Command": "XType",
  "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "XType",
  "Target": "${KEY_ENTER}",
  "Value": "",
  "Description": "Returning to main page"
},
{
  "Command": "pause",
  "Target": "3000",
  "Value": "",
  "Description": "Pausing 3 secs to refresh after it"
},
{
  "Command": "else",
  "Target": "",
  "Value": "",
  "Description": "Actions if download page doesn´t exist"
},
{
  "Command": "echo",
  "Target": "No new page opened.",
  "Value": "red",
  "Description": "Echo for no new page opened"
},
{
  "Command": "click",
  "Target": "id=requestAccounts",
  "Value": "",
  "Targets": [
    "id=requestAccounts",
    "xpath=//*[@id=\"requestAccounts\"]",
    "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
    "xpath=//mds-navigation-bar-item",
    "css=#requestAccounts"
  ],
  "Description": "Returning to main page when there aren´t movements"
},
{
  "Command": "end",
  "Target": "",
  "Value": "",
  "Description": "Closing if condition"
},




    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 9972"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 9972"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },





    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 9552"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 9552"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },





    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 3205"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 3205"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },






    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 1117"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 1117"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },



    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 0689"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 0689"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },





    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 3832"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 3832"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },




    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 7321"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 7321"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    },






    {
      "Command": "comment",
      "Target": "CODE FOR ANOTHER ACCOUNT",
      "Value": "",
      "Description": ""
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "XType",
      "Target": "${KEY_F5}",
      "Value": "",
      "Description": "Refreshing the web page 2"
    },
    {
      "Command": "pause",
      "Target": "3500",
      "Value": "",
      "Description": "Pausing to refresh again and avoid issues"
    },
    {
      "Command": "click",
      "Target": "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
      "Value": "",
      "Targets": [
        "xpath=//*[@id=\"allAccountsOverview\"]/div/div/div[2]",
        "xpath=//div[6]/div/div/div/div[2]",
        "css=#allAccountsOverview > div.filter-container-block > div > div.filter-container.mds-row.mds-d-flex.mds-jc-space-between.mds-fw-wrap"
      ],
      "Description": "Clicking to focus the page"
    },
    {
      "Command": "bringBrowserToForeground",
      "Target": "",
      "Value": "",
      "Description": "This is to update the focus on Chase web page (it is useful for tab)"
    },

    {
      "Command": "click",
      "Target": "id=seeAllAccountsAG1Table",
      "Value": "",
      "Targets": [
        "id=seeAllAccountsAG1Table",
        "xpath=//*[@id=\"seeAllAccountsAG1Table\"]",
        "xpath=//mds-link[@id='seeAllAccountsAG1Table']",
        "xpath=//mds-link",
        "css=#seeAllAccountsAG1Table"
      ],
      "Description": "Clicking \"See all accounts\""
    },


    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB} ${KEY_TAB}  ${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}${KEY_TAB}",
      "Value": "",
      "Description": "Selecting bank account 2289"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Selecting bank account 2289"
    },
    {
      "Command": "click",
      "Target": "id=headerSearchLink",
      "Value": "",
      "Targets": [
        "id=headerSearchLink",
        "xpath=//*[@id=\"headerSearchLink\"]",
        "xpath=//mds-link[@id='headerSearchLink']",
        "xpath=//div[3]/mds-link",
        "css=#headerSearchLink"
      ],
      "Description": "Searching"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ${KEY_TAB}",
      "Value": "",
      "Description": "Selecting from date"
    },
    {
      "Command": "XType",
      "Target": "${FromDate}",
      "Value": "",
      "Description": "Typing from date"
    },
    {
      "Command": "XType",
      "Target": "${KEY_TAB} ${KEY_TAB} ",
      "Value": "",
      "Description": "Selecting to date"
    },
    {
      "Command": "XType",
      "Target": "${ToDate}",
      "Value": "",
      "Description": "Typing to date"
    },
    {
      "Command": "click",
      "Target": "id=activitySearchFilter",
      "Value": "",
      "Targets": [
        "id=activitySearchFilter",
        "xpath=//*[@id=\"activitySearchFilter\"]",
        "xpath=//mds-button[@id='activitySearchFilter']",
        "xpath=//div[2]/div[2]/mds-button",
        "css=#activitySearchFilter"
      ],
      "Description": "Clicking search after indicating dates"
    },
    {
      "Command": "pause",
      "Target": "2000",
      "Value": "",
      "Description": "Pausing to avoid issues"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "initialTitle",
      "Description": "Checking initialTitle"
    },
    {
      "Command": "echo",
      "Target": "The page title is ${initialTitle}\t",
      "Value": "",
      "Description": "Echo for initialTitle"
    },
    {
      "Command": "click",
      "Target": "id=downloadActivityIcon",
      "Value": "",
      "Targets": [
        "id=downloadActivityIcon",
        "xpath=//*[@id=\"downloadActivityIcon\"]",
        "xpath=//mds-button[@id='downloadActivityIcon']",
        "xpath=//span[2]/mds-button",
        "css=#downloadActivityIcon"
      ],
      "Description": "Clicking download buttom"
    },
    {
      "Command": "storeTitle",
      "Target": "",
      "Value": "afterClickTitle",
      "Description": "Checking afterClickTitle"
    },
    {
      "Command": "if",
      "Target": "${initialTitle} != ${afterClickTitle}",
      "Value": "",
      "Description": "Evaluating if download page is open"
    },
    {
      "Command": "echo",
      "Target": "New page opened.",
      "Value": "green",
      "Description": "Echo if new page opened"
    },
    {
      "Command": "click",
      "Target": "id=download",
      "Value": "",
      "Targets": [
        "id=download",
        "xpath=//*[@id=\"download\"]",
        "xpath=//mds-button[@id='download']",
        "xpath=//div[2]/mds-button",
        "css=#download"
      ],
      "Description": "Downloading report"
    },
    {
      "Command": "XType",
      "Target": "${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}${KEY_SHIFT+KEY_TAB}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "XType",
      "Target": "${KEY_ENTER}",
      "Value": "",
      "Description": "Returning to main page"
    },
    {
      "Command": "pause",
      "Target": "3000",
      "Value": "",
      "Description": "Pausing 3 secs to refresh after it"
    },
    {
      "Command": "else",
      "Target": "",
      "Value": "",
      "Description": "Actions if download page doesn´t exist"
    },
    {
      "Command": "echo",
      "Target": "No new page opened.",
      "Value": "red",
      "Description": "Echo for no new page opened"
    },
    {
      "Command": "click",
      "Target": "id=requestAccounts",
      "Value": "",
      "Targets": [
        "id=requestAccounts",
        "xpath=//*[@id=\"requestAccounts\"]",
        "xpath=//mds-navigation-bar-item[@id='requestAccounts']",
        "xpath=//mds-navigation-bar-item",
        "css=#requestAccounts"
      ],
      "Description": "Returning to main page when there aren´t movements"
    },
    {
      "Command": "end",
      "Target": "",
      "Value": "",
      "Description": "Closing if condition"
    }


    


    


    


    


    


    