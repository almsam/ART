// Import the function to be tested
const { sendRequest } = require('./yourScriptFileName.js'); // Assuming your script is in a separate file

// Mock the fetch function
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve({ responseData: 'mock data' }),
  })
);

describe('sendRequest', () => {
  beforeEach(() => {
    // Clear the mock implementation before each test
    fetch.mockClear();
  });

  it('sends a request with the correct action', async () => {
    // Call the function
    await sendRequest('testAction');

    // Check if fetch was called with the correct URL and options
    expect(fetch).toHaveBeenCalledWith('/api/testAction', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
    });
  });

  it('handles a successful response', async () => {
    // Call the function
    const result = await sendRequest('testAction');

    // Check if it returns the correct data
    expect(result).toEqual({ responseData: 'mock data' });
  });

  it('handles an unsuccessful response', async () => {
    // Mock fetch to return an unsuccessful response
    global.fetch.mockImplementationOnce(() =>
      Promise.resolve({
        ok: false,
        status: 400,
        statusText: 'Bad Request',
      })
    );

    // Call the function
    await sendRequest('testAction');

    // Check if it logs the error message
    expect(console.error).toHaveBeenCalledWith('There was a problem with your fetch operation:', expect.any(Error));
  });
});