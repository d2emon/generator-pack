"""
================
Nested by Orteil
================
[ http://orteil.deviantart.com , https://twitter.com/Orteil42 , orteil42@gmail.com - more stuff like this at http://orteil.dashnet.org ]
This is the source-code. Use it wisely. (Better not use it without my permission though.)

I made this when I was bored at work around 2011; I've been progressively adding stuff to it since.
I am by no means a professional programmer (I do pixel-art and game-design), so please don't judge my code too harshly!

Wikipedia was used extensively for this project. I am now aware of the composition of everything. *Everything*.

(oh yeah, don't read all the code right now, it kind of ruins the surprise of finding things!)
"""
import random

from .thing import Thing
from .item import Item


"""
function WeightedChoose(arr,weightChoose)
{
	//Returns an element from an array at random according to a weight.
	//A weight of 2 means the first element will be picked roughly twice as often as the second; a weight of 0.5 means half as often. A weight of 1 gives a flat, even distribution.
	if (weightChoose<=0 || weightChoose==undefined) weightChoose=1;
	return arr[Math.floor(Math.pow(Math.random(),weightChoose)*arr.length)];
	
	//return arr[Math.floor((1-Math.pow(Math.random(),1/weightChoose))*arr.length)];//this would give a different curve

	//previously
	/*
	var iChoose;
	var arrChoose=[];
	if (weightChoose<=0 || weightChoose==undefined) weightChoose=1;
	for (iChoose=0;iChoose<arr.length;iChoose++)
	{
		if (Math.round(Math.random()*(iChoose*weightChoose))==0) arrChoose.push(arr[iChoose]);
	}
	return Choose(arrChoose);
	*/
}


function CheckMissingThings()
{
	var allContents=[];
	var allMissing=[];
	for (var i in Things)
	{
		var thisThing=Things[i];
		for (var i2 in thisThing.contains)
		{
			thisContent=thisThing.contains[i2];
			if (typeof(thisContent)!="string")
			{
				for (var i3 in thisContent) {allContents.push(thisContent[i3]);}
			}
			else allContents.push(thisContent);
		}
	}
	for (var i in allContents)
	{
		var thisContent=allContents[i];
		if (thisContent.charAt(0)==".") thisContent=thisContent.substring(1);
		thisContent=thisContent.split(",");
		thisContent=thisContent[0];
		if (!Things[thisContent] && thisContent!="") allMissing.push(thisContent);
	}
//	allMissing=allMissing.filter(function(elem,pos) {return allMissing.indexOf(elem)==pos;});//remove duplicates

	var str="Things that are linked to, but don't exist :\n";
	for (var i in allMissing)
	{
		str+=allMissing[i]+"\n";
	}
	alert(str);
}

function Title(what)
{
	//Changes a string like "the cat is on the table" to "the Cat Is on the Table"
	what=what.split(" ");
	var toReturn="";
	for (var i in what)
	{
		if (what[i]!="of" && what[i]!="in" && what[i]!="on" && what[i]!="and" && what[i]!="the" && what[i]!="an" && what[i]!="a" && what[i]!="with" && what[i]!="to" && what[i]!="for") what[i]=what[i].substring(0,1).toUpperCase()+what[i].substring(1);
		toReturn+=" "+what[i];
	}
	return toReturn.substring(1);
}
"""


def choose__(arr):
    return random.choice(arr)


def weighted_choose__(arr, weightChoose):
    pass


def rand__(a, b):
    return random.randrange(a, b)


def check_missing_things__():
    pass


def title__(what):
    pass