Markdown notes maintained in Obsidian for resources to learn ASL.

The project requires Python 3 to import flashcards. To setup the environment for the project, run:
```bash
make setup
```

To import flashcards, pull a CSV in [this format](https://docs.google.com/spreadsheets/d/1wntkF6W-mNdyTxaEZI-RmvvdGeeDKY8iq9FHbYhtNog/edit?usp=sharing).
Then, import the flashcards by running a target such as:
```bash
make asl-101-flashcards
```

## Anki Scripts & Style
Cards exported to Anki have the following scripts and style.
```js
const htmlCollection = document.getElementsByTagName('*');

function showSubsequentElements(elementToHide, elementsToShow) {
	let beginShowing = false
	for (const node of htmlCollection) {
		const nodeType = typeof node.nodeName === 'string'
			? node.nodeName.toLowerCase()
			: null;
		if (nodeType === 'button') {
			beginShowing = elementToHide.id === node.id;
		}
		if (beginShowing && elementsToShow.includes(nodeType)) {
			node.style.display = 'none';
			node.style.display = 'revert';
		}
	}
	elementToHide.style.display = 'none';
}
```

```css
h5 {
	margin-top: 40px;
	margin-bottom: -30px;
}
button {
	margin-top: 20px;
}
```

### Card-Spaced Note Type
```js
function showSign(e) {
	showSubsequentElements(e, ['img', 'a', 'pre']);
}
```

```css
a, img, pre {
	display: none;
}
a {
	font-size: 12px;
}
```

### Card/Reverse Note Type
```js
function showTranscript(e) {
	showSubsequentElements(e, ['a']);
}
```

```css
a {
	pointer-events: none;
	font-size: 13px;
	display: none;
}
```