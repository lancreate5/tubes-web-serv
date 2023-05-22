// Aliases
let query = (tag) => document.querySelector(tag);
let selectCls = (cls) => document.getElementsByClassName(cls)[0];
let onClick = (obj, fn) => obj.addEventListener("click", fn);
let onHover = (obj, fn) => obj.addEventListener("mouseover", fn);
let onOut = (obj, fn) => obj.addEventListener("mouseout", fn);

color = [
	// wholeBG |   text   |   box    | Highlighting
	["#2b2a33", "#FFFFFF", "#42414d"],
	["#BDBDBD", "#000000", "#FFFFFF"]
]

let token = 0;
let button = selectCls("swap-color");
let eventID;

onHover(button, () => {
		eventID = setInterval(() => {
			token = (token + 1) % 2;

			query("body").style.background = color[token][0];

			let box = selectCls("wrap");
			box.style.background = color[token][2];

			button.style.color = color[token][1];
			button.style.background = color[token][0];

			let content = selectCls("content").children;
			for(let i = 0; i < content.length; i++) {
				content[i].style.color = color[token][1];
			}
		},
		100);
	}
);

onOut(button, () => clearInterval(eventID));
