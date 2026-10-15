<img src="./power_player.png" style="width:100%">

# Power Player
**Power Player** is a runtime player that executes code and assets authored in PowerPoint, enabling the development of games, interactive media.

- Standalone : Windows / Linux / MacOS

# Instructions
## 1. Visual Editing
Edit objects directly on the slides. Define object names and layer hierarchy using the **Selection Pane** *(Home > Select > Selection Pane)*.

## 2. Scripting
Write `JavaScript` directly in the slide's **Comment section** to control objects, set up game loops, and handle player input.

- Invoke the function with **'this'** as the **Game Instance**.
- Using **this.var["varName"]** / **this.var.varName** to defined a global(Game) variable.
- Using **let / var** to defined a temporary variable.
- Auto convert `”` `“` to `'`, `’` `‘` to `'`.
- Using **[spawnObject](./Docs/api.md#spawnobject)** to duplicate an object results in a new instance named with the format `[originalName]-[uuid]`.
- ***Disable auto correct option : `File -> Options -> Proofing -> AutoCorrect Options`***
- A semicolon `;` is required at the end of each statement.
- When switching slides, **the audio will not stop or release its resources**. Call **[releaseAllAudio](./Docs/api.md#releaseallaudio)** to stop and release all audio.
- **System functions of the Game :**
    - **[onLoaded](./Docs/api.md#onloaded)**
    - **[onStart](./Docs/api.md#onstart)**
    - **[onUpdate](./Docs/api.md#onupdate)**
    - **[onEnd](./Docs/api.md#onend)**
- **Save & Load :**

    The saved data will be stored in the PowerPlayer application path.
    - **[save](./Docs/api.md#save)** : Save all the values belonging to `this.var`.
    - **[load](./Docs/api.md#load)** : Load the values and set to `this.var`.
- **Switch / Restore Slides** : Preserves the state of the previous slide when switching, and restores it using `returnSlide`.

## 3. Execution Flow
- ### Switch Slide
    `Code -> (async)onLoaded -> (async)onStart -> onUpdate -> (async)onEnd`
- ### Return Slide
    `(async)onStart -> onUpdate -> (async)onEnd`

### Class & Functions
- `Class`
    - [Game](./Docs/api.md#game)
    - [Input](./Docs/api.md#inputclass)
    - [InputStatus](./Docs/api.md#inputstatus)
- **Scenes**
    - [switchSlide](./Docs/api.md#switchslide)
    - [returnSlide](./Docs/api.md#returnslide)
- **Scene Objects**
    - [getObject](./Docs/api.md#getobject)
    - [queryObjects](./Docs/api.md#queryobjects)
    - [removeObject](./Docs/api.md#removeobject)
    - [addToGroup](./Docs/api.md#addtogroup)
    - [getGroup](./Docs/api.md#getgroup)
    - [getObjectOrGroup](./Docs/api.md#getobjectorgroup)
    - [removeFromGroup](./Docs/api.md#removefromgroup)
    - [spawnObject](./Docs/api.md#spawnobject)
    - [animate](./Docs/api.md#animate)
- **Collision**
    - [collide](./Docs/api.md#collide)
    - [objectOutOfScene](./Docs/api.md#objectoutofscene)
- **Audio**
    - [playAudio](./Docs/api.md#playaudio)
    - [stopAudio](./Docs/api.md#stopaudio)
    - [stopAllAudio]()
    - [releaseAllAudio]()
- **Input**
    - [Input](./Docs/api.md#input)
    - [InputStatus](./Docs/api.md#inputstatus)
- **Save/Load**
    - [save](./Docs/api.md#save)
    - [load](./Docs/api.md#load)

## 3. Objects
 - [Image (Sprite)](./Docs/api.md#sprite)
 - [Text](./Docs/api.md#text)
 - [Group](./Docs/api.md#group)

# Example
- Make a button and switch to other slides
    ``` JavaScript
    {
        let b = this.getObject("buttonObject");
        b.interactive=true;
        b.on("pointerdown",()=>{
            this.switchSlide(2);
        })
    }
    ```

- Control player
    ``` JavaScript
    this.onUpdate=(delta)=>{
        let player = this.getObject("player");
        player.x = this.input.mousePosition.x;
        player.y = this.input.mousePosition.y;
        if(this.input.getCode("KeyA")=="JustPress"){
            this.spawnObject("object", {x:p.x+60, y:p.y});
            this.playAudio(0,"se");
        }
    }
    ```

- Update spawned objects
    ``` JavaScript
    this.onUpdate=(delta)=>{
        for(let obj of this.queryObjects("^objects-.+$")){
            obj.x+=delta*300;
            if(this.objectOutOfScene(obj.name)){
                this.removeObject(obj.name);
            }
            else if(this.collide("player",obj.name)){
                this.var["score"]+=1;
                this.removeObject(obj.name);
            }
        }
    }
    ```
- Animation
    ``` typescript
    this.onLoaded = async ()=>{
        await this.animate("player",{x:100},1000);
    }
    ```
- Save / Load
    ``` typescript
    let saveButton = this.getObject("saveButton");
    saveButton.interactive=true;
    saveButton.on("pointerdown",async ()=>{
        this.var.name = "(っ °Д °;)っ";
        await this.save();
        delete this.var.name;
    });

    let loadButton = this.getObject("loadButton");
    loadButton.interactive=true;
    saveBloadButtonutton.on("pointerdown",async ()=>{
        await this.load();
        this.getObject("nameText").text = this.var.name;
    });
    ```
# Demo
- #### Editing & Scripting.
    <img src="./screenshots/powerplayer_demo_1.gif" style="width:100%;max-width:480px">
- #### Gameplay
    <img src="./screenshots/powerplayer_demo_2.gif" style="width:100%;max-width:480px">
