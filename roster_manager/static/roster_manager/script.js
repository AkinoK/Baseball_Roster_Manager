// Wait for the DOM content to be fully loaded before executing the code
document.addEventListener("DOMContentLoaded", function() {
    // Check if the page is roster_list.html before calling DeleteButtons
    if (window.location.pathname.endsWith('roster_list/')) {
        DeleteButtons();
    }

    // Check if the #id_position element exists before calling PositionSelect
    if (document.querySelector('#id_position')) {
        PositionSelect();
    }
});

// ...


// Handle position selection
function PositionSelect() {

    // Define the ID for the pitcher position
    const pitcherPositionId = 1;

    // Get references to DOM elements
    const positionSelect = document.getElementById("id_position");
    const pitchingWinsField = document.getElementById("id_pitching_wins");
    const pitchingLossesField = document.getElementById("id_pitching_losses");
    const eraField = document.getElementById("id_era");

    // Add an event listener to the position select element
    positionSelect.addEventListener("change", function() {
        
        if (positionSelect.value === String(pitcherPositionId)) {
            // Enable the fields for pitching statistics
            pitchingWinsField.disabled = false;
            pitchingLossesField.disabled = false;
            eraField.disabled = false;
        } else {
            // Disable the fields for pitching statistics
            pitchingWinsField.disabled = true;
            pitchingLossesField.disabled = true;
            eraField.disabled = true;
        }
    });
}


function DeleteButtons() {
    const deleteButtons = document.querySelectorAll(".delete-player-icon");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function(event) {
            // Prevent the default click behavior
            event.preventDefault();

            // Get the player's name from the data attribute
            const playerName = button.getAttribute("data-player-name");
            console.log(playerName);

            // Update the modal with the player's name
            document.getElementById("playerNameToDelete").textContent = playerName;

            // Store the player's ID in a data attribute
            const playerId = button.getAttribute("data-player-id");
            document.getElementById("deletePlayerLink").setAttribute("data-player-id", playerId);

            // Update the delete link's href attribute with the player ID
            const deleteLink = document.getElementById("deletePlayerLink");
            deleteLink.setAttribute("href", `/roster_manager/delete_player/${playerId}/`);


        });
    });

    

    // Add a click event listener to the "Delete" link in the modal
    const deletePlayerLink = document.getElementById("deletePlayerLink");
    deletePlayerLink.addEventListener("click", function() {
        const playerId = deletePlayerLink.getAttribute("data-player-id");
        const deleteURL = `/roster_manager/delete_player/${playerId}/`;
    
        // Perform the deletion by making a POST request
        fetch(deleteURL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'), // Get CSRF token from cookies
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.reload(); 
            } else {
                console.error("An error occurred:", data.message);
            }
        })
        .catch(error => {
            console.error("An error occurred:", error);
        });
    });
    
}

// Function to get CSRF token from cookies
function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;) ?' + name + '=([^;]*)(;|$)');
    return cookieValue ? cookieValue[2] : null;
}
