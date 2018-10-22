// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage

module.exports = {
  'default e2e tests': function (browser) {
    // automatically uses dev Server port from /config.index.js
    // default: http://localhost:8080
    // see nightwatch.conf.js
    const devServer = browser.globals.devServerURL

    browser
      .url(devServer)
      .waitForElementVisible('body', 1000)
      .assert.title('ProductDevelopmentProject')
      .assert.containsText('h4', 'Risks')
      .click('a[id=Fields]')
      .pause(1000)
      .assert.containsText('h4', 'Fields')
      .click('a[id=CreateField]')
      .pause(1000)
      .assert.containsText('h1', 'Create a Field')
      .click('a[id=RiskTypes]')
      .pause(1000)
      .assert.containsText('h4', 'RiskTypes')
      .click('a[id=CreateRiskType]')
      .pause(1000)
      .assert.containsText('h1', 'Create a RiskType')
      .click('a[id=Risks]')
      .pause(1000)
      .assert.containsText('h4', 'Risks')
      .click('a[id=CreateRisk]')
      .pause(1000)
      .assert.containsText('h1', 'Create a Risk')
      .assert.elementCount('img', 0)
      .end()
  }
}
