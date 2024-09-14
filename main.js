function checkAvailability() {
    // Get the selected parking lot ID
    const lotId = document.getElementById('lot-id').value;
  
    // Simulate available parking spots for each lot
    let availableSpots;
    
    if (lotId === "1") {
      // For First lot, simulate 10 to 30 available spots
      availableSpots = Math.floor(Math.random() * (30 - 10 + 1)) + 10;
    } else if (lotId === "2") {
      // For Second lot, simulate 5 to 20 available spots
      availableSpots = Math.floor(Math.random() * (20 - 5 + 1)) + 5;
    }
  
    // Show the simulated available spots in the #parking-info div
    document.getElementById('parking-info').innerText = `Available spots: ${availableSpots}`;
  }
  
  