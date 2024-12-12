document.addEventListener("DOMContentLoaded", function () {
    // Select all elements with the class 'show-text'
    const yesElements = document.querySelectorAll(".show-text");
    const infoBox = document.getElementById("info-box");
    const infoText = document.getElementById("info-text");
  
    yesElements.forEach((element) => {
      element.addEventListener("click", function () {
        // Retrieve the text from the 'data-text' attribute
        const text = this.getAttribute("data-text");
  
        // Set the text in the info box
        infoText.textContent = text;
  
        // Position the box relative to the clicked element
        const rect = this.getBoundingClientRect();
        infoBox.style.position = "absolute";
        infoBox.style.top = `${rect.top + window.scrollY}px`;
        infoBox.style.left = `${rect.right + 10}px`;
  
        // Show the info box
        infoBox.style.display = "block";
      });
    });
  
    // Hide the box when clicked outside
    document.addEventListener("click", function (event) {
      if (!infoBox.contains(event.target) && !event.target.classList.contains("show-text")) {
        infoBox.style.display = "none";
      }
    });
  });
  
