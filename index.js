const { Builder, Key } = require("selenium-webdriver");

const firefox = require("selenium-webdriver/firefox");
const options = new firefox.Options();
options.setPreference("browser.download.dir", "C:\\")

const driver = new Builder().forBrowser("firefox").build();
//driver.build(); //launch browser
driver.get("https://google.com"); // get any link

//firefox Profile
//free proxy 
