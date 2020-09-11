# WordCloud
 Convert your WhatsApp chats into a WordCloud. The script will automatically detect the most used words from your chat and add them to the WordCloud.

 ## Libraries / Modules
  1. NumPy
  2. Pandas
  3. OS
  4. PIL
  5. WordCloud
  6. MatPlotLib
  7. Random
 
 ## Steps To Use
 * Clone this directory onto your local machine.
 * Install the required dependencies/modules/libraries incase you haven't already.
 * Export your WhatsApp chat (without media). Look up online if you do not not how to do this.
 * Paste the chat in the root of the cloned directory and rename it `text.txt`.
 * There are a few masks already present inside the "Masks" folder. One of these masks will be randomly selected and applied to your worldcloud.
 * You can add your own custom mask too. The image that you wish to use as a mask has to be added to the "Masks" folder.
 * Then edit `line 57` of WordCloud.py
    ```
    mask = np.array(Image.open("Masks/Mask"+str(random.randrange(1,11))+".jpg"))
    ```
    Replace `"Masks/Mask"+str(random.randrange(1,11))+".jpg"` with the address of your preferred image. For exapmle, `"Masks/Custom.jpg"`
    ```
    mask = np.array(Image.open("Masks/Custom.jpg"))
    ```
 * After either choosing to apply your own custom mask or choosing to stick to the default ones, just run the WordCloud.py script.
 * Cheers! Happy Coding!
 ## License
 ### Created by Aryan Felix
 ### © MIT License