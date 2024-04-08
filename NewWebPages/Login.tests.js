describe('validateCredentials', () => {
    it('returns true for correct credentials', () => {
      expect(validateCredentials('your_database_username', 'your_database_password')).toBe(true);
    });
  
    it('returns false for incorrect credentials', () => {
      expect(validateCredentials('incorrect_username', 'incorrect_password')).toBe(false);
    });
  });