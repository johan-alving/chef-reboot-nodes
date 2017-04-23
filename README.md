# Trigger a reboot during next chef-client run
This Python script will trigger a reboot during the next chef-client run for all or a subset of nodes. It works by applying a tag to the nodes specified. The tag is defined by `REBOOT_TAG`. To actually make a node reboot after having been tagged, its run list needs to contain a recipe which checks if it is tagged, and then use the "reboot" resource. For an example on this kind of recipe, see reboot.rb.

There are 2 constants in the script:

- `CHEF_REPO` - Path to your local Chef repo that contains the ".chef" folder
- `REBOOT_TAG` - The tag that will be applied to the nodes. This needs to match the tag used in the reboot recipe in the run list.

## How to use it

To reboot all nodes:
```
python reboot_nodes.py --all
```

You can also reboot nodes using wildcards:
```
python reboot_nodes.py --wildcard x64-linux*
```
