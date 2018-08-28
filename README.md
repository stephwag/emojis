Script to handle strings with emojis using the [data from unicode.org](https://unicode.org/Public/emoji/11.0/emoji-data.txt) (updated on 2018-02-07).

#### Example

```
from emojis import has_emoji, get_emojis

# Checks if a string contains an emoji.
has_emoji("Hey look, an emoji 😄")
=> True

# Returns a list of emojis and their indices from the string.
get_emojis("Hey look, an emoji 😄, and here's another one 👍.")
=> [(45, '👍'), (19, '😄')]
```
