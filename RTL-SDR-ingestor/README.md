cusignal-nifi Nar wrapper for cusignal 
====================================

Conda installation:

# todo: use the new cusignal installation guide to setup env.

conda 4.7.x is a bit wonlky  with the commands, sometimes it accepts `--name` in all envrinoment changes and others it must be  `-n=` [1] 

Ensurr that conda is correctly configured for your system.

Set `always_yes` to *true*, or you'll have prompts while running `make`.

```
# ######################################################
# ##  Output, Prompt, and Flow Control Configuration  ##
# ######################################################

# # always_yes (NoneType, bool)
# #   aliases: yes
# #   Automatically choose the 'yes' option whenever asked to proceed with a
# #   conda operation, such as when running `conda install`.
# #always_yes:
```



this will put you into the `cusignal-nifi` virtual envronments and install all python dependencies.
to build using make.  run: 
```bash
$make env 
$make xxx 
```

Alternatively, you can run `make all`




[1] https://github.com/conda/conda/issues/8205
