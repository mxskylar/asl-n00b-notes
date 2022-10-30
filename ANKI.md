# Anki
## Scripts & Style
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
	margin-top: 50px;
}
.toggle-button-padding {
	visibility: hidden;
}
```

## Card-Spaced Note Type
```js
function showSign(e) {
	showSubsequentElements(e, ['img', 'a', 'pre']);
}
```

```css
a, img, pre {
	display: none;
}
```

## Card/Reverse Note Type
```js
function showTranscript(e) {
	showSubsequentElements(e, ['a']);
}
```

```css
a {
	pointer-events: none;
	display: none;
}
```