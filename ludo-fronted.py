ludo-frontend/
├── index.html
<!DOCTYPE html>
<html>
<head>
  <title>Ludo Game</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>🎲 Ludo Game 🎲</h1>

  <div id="signup">
    <h2>Signup</h2>
    <input type="email" id="email" placeholder="Enter Email">
    <input type="password" id="password" placeholder="Enter Password">
    <button onclick="signup()">Signup</button>
  </div>

  <div id="game" style="display:none;">
    <h2>Welcome to Ludo!</h2>
    <canvas id="board" width="400" height="400"></canvas>
  </div>

  <script src="game.js"></script>
</body>
</html>
├── style.css
/* Ludo Game Styling */
body { 
  font-family: Arial, sans-serif; 
  text-align: center; 
  background: #f2f2f2; 
}
h1 { color: green; }
#signup, #game { margin-top: 20px; }

/* Optional: input & button styling */
input { padding: 8px; margin: 5px; }
button { padding: 8px 12px; cursor: pointer; background: green; color: white; border: none; border-radius: 4px; }
button:hover { background: darkgreen; }
└── game.js
// Signup function (frontend)
function signup() {
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  if(!email || !password){
    alert("Please enter email and password");
    return;
  }

  fetch("https://<railway-backend-url>/signup", {  // Replace with your Railway URL
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  })
  .then(res => res.json())
  .then(data => {
    if(data.success){
      alert("Signup Successful!");
      document.getElementById("signup").style.display = "none";
      document.getElementById("game").style.display = "block";
      startGame();
    } else {
      alert("Signup Failed!");
    }
  })
  .catch(err => console.error(err));
}

// Simple Ludo canvas demo
function startGame() {
  const canvas = document.getElementById("board");
  const ctx = canvas.getContext("2d");

  // Draw simple Ludo board (placeholder)
  ctx.fillStyle = "#FFD700";
  ctx.fillRect(0, 0, 400, 400);

  ctx.fillStyle = "#FF0000";
  ctx.fillRect(0, 0, 100, 100); // Top-left red square
  ctx.fillStyle = "#0000FF";
  ctx.fillRect(300, 0, 100, 100); // Top-right blue square
  ctx.fillStyle = "#00FF00";
  ctx.fillRect(0, 300, 100, 100); // Bottom-left green square
  ctx.fillStyle = "#FFFF00";
  ctx.fillRect(300, 300, 100, 100); // Bottom-right yellow square

  ctx.fillStyle = "#000";
  ctx.font = "20px Arial";
  ctx.fillText("Ludo Board Demo", 120, 200);
}