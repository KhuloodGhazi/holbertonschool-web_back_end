export default class Building {
  constructor(sqft) {
    // Prevent direct instantiation of Building
    if (new.target === Building) {
      throw new Error('Building is an abstract class and cannot be instantiated directly');
    }

    this._sqft = sqft;

    // Ensure subclass overrides evacuationWarningMessage
    if (this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage) {
      throw new Error('Class extending Building must override evacuationWarningMessage');
    }
  }

  // Getter and setter for sqft
  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }

  // Abstract method
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
