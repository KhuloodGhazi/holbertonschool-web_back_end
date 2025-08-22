export default class Building {
  constructor(sqft) {
    this._sqft = sqft;

    // Ensure subclasses override evacuationWarningMessage
    if (
      this.constructor !== Building &&
      this.evacuationWarningMessage === Building.prototype.evacuationWarningMessage
    ) {
      throw new Error(
        'Class extending Building must override evacuationWarningMessage'
      );
    }
  }

  // Getter and setter
  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }

  // "Abstract" method — must be overridden by subclass
  evacuationWarningMessage() {
    throw new Error(
      'Class extending Building must override evacuationWarningMessage'
    );
  }
}
