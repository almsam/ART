// Import the function to be tested
const { validateForm } = require('./yourScriptFileName.js'); // Assuming your script is in a separate file

describe('validateForm', () => {
  let originalAlert;

  beforeAll(() => {
    // Mock the alert function to prevent actual pop-ups
    originalAlert = global.alert;
    global.alert = jest.fn();
  });

  afterAll(() => {
    // Restore the original alert function after all tests are done
    global.alert = originalAlert;
  });

  it('returns true for valid input', () => {
    // Set up the DOM environment using JSDOM
    document.body.innerHTML = `
      <input id="username" value="testuser">
      <input id="password" value="password123">
      <input id="confirmPassword" value="password123">
      <input id="email" value="test@example.com">
      <input id="dob" value="2000-01-01">
    `;

    // Call the function
    const result = validateForm();

    // Assert that the function returns true for valid input
    expect(result).toBe(true);

    // Assert that alert was not called
    expect(global.alert).not.toHaveBeenCalled();
  });

  it('alerts error messages for invalid input', () => {
    // Set up the DOM environment using JSDOM
    document.body.innerHTML = `
      <input id="username" value="testuser">
      <input id="password" value="123"> <!-- Invalid password length -->
      <input id="confirmPassword" value="password123">
      <input id="email" value="testexample.com"> <!-- Invalid email format -->
      <input id="dob" value="2050-01-01"> <!-- Date of birth in the future -->
    `;

    // Call the function
    const result = validateForm();

    // Assert that the function returns false for invalid input
    expect(result).toBe(false);

    // Assert that alert was called with correct error messages
    expect(global.alert).toHaveBeenCalledWith(expect.stringContaining("Password must be at least 7 characters long"));
    expect(global.alert).toHaveBeenCalledWith(expect.stringContaining("Invalid email format"));
    expect(global.alert).toHaveBeenCalledWith(expect.stringContaining("Date of birth must be in the past"));
  });
});