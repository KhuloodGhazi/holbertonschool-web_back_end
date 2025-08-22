import Building from './5-building.js';

describe('Building forces override', () => {
  test('subclass must override evacuationWarningMessage', () => {
    class TestBuilding extends Building {}
    
    // Use .toThrow instead of .toThrowError
    expect(() => {
      new TestBuilding(200);
    }).toThrow('Class extending Building must override evacuationWarningMessage');
  });

  test('subclass with overridden method works', () => {
    class SafeBuilding extends Building {
      evacuationWarningMessage() {
        return 'Evacuate immediately!';
      }
    }

    const b = new SafeBuilding(300);
    expect(b.sqft).toBe(300);
    expect(b.evacuationWarningMessage()).toBe('Evacuate immediately!');
  });
});
