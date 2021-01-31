main:
    "Welcome to narrat, the narrative game engine"
    talk cat idle "\"That was the game speaking, but you can also make characters speak! \""
    // This is a comment
    set someValue 2 // You can set any values in the data part of the state
    $if this.data.someValue === 1: // You can do conditions on the state
        "This line shouldn't appear because someValue is 2"
    talk cat idle "\"You can have branching choices and skillchecks\""
    choice: // Branching choices
        talk cat idle "\"What's up'\"" // This is the prompt for the choice
        "\"Nothing\"": // This is the first option
            talk cat idle "\"Ah ok, that's cool\""
        skillcheck skillCheckInChoice testSkill 40 "Say something if a skill check works": // The second option is a skill check
            success "\"Hey I passed a skill check\" (this is appearing because a skill check succeeded)": // This happens if the skill check succeeds
                talk cat idle "\"wow that's cool\""
            failure "You failed the skill check":
    talk cat idle "\"To view the code used for this demo \"story\", look in the `example.rpy` file in the narrat-template folder.\""
    talk cat idle "\"It's also possible to separate your code in multiple labels to organise it. Let's jump to a different label\""
    jump testLabel

choicesDemo:
    talk cat idle "\"We can also store data when you make choices\""
    choice:
        talk cat idle "\"Do you like choices?\""
        "Yes":
            set likeChoices true
        "No":
            set likeChoices false
    choice:
        talk cat idle "\"What should we do today?\""
        "let's make choices cause I like making choices!" $if this.data.likeChoices: // A choice can have a condition so it only appears in the list if the condition is met
            talk cat idle "\"See, you were only able to select this option because you said you like choices earlier /""
        "let's do nothing!":
            talk cat idle "\"ok :( If this was your only option, it's because you said you didn't like choices earlier.\""
    talk cat idle "\"Some dialogue can also only appear if you pass a condition, for example a skill check\""
    $if this.skillCheck("skillCheckDemo", "testSkill", 40): // You can use skillchecks in conditions
        "This line only appears because a skill check succeeded"
    else:
        "This line appears because a skill check failed"
    jump savingAndLoading

testLabel:
    talk cat idle "Hello, this dialogue exists in a different label so you can keep your files organised."
    jump choicesDemo
// Different labels can also be in different files

savingAndLoading:
    talk cat idle "\"The engine also supports saving and loading. It keeps track of your stats and data, and skill checks you've passed or failed.\""
    talk cat idle "\"If you reload the page now and choose to continue the game, it will continue at the last label that was played, but will keep skill checks locked if you failed them, or skip them if you succeeded.\""
    talk cat idle "\"The game autosaves after every choice.\""
    talk cat idle "\"Now that's it for the demo, we're going back to the intro. Feel free to test things out and see how saving and reloading works.\""
    talk cat idle "\"Then you can use the `narrat-template` repo as a base to start your own game. It's all ready to use and modify.\""
    jump main