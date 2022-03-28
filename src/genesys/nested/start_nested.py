

__things = {}


def __clean_things():
    """
	for (var iT in Things)
	{
		thisT=Things[iT];

		toConcat=[];
		for (var i in thisT.contains)
		{
			if (typeof(thisT.contains[i])=="string")
			{
				if (thisT.contains[i].charAt(0)==".")
				{
					if (Things[thisT.contains[i].substring(1)]!=undefined)
					{
						toConcat=toConcat.concat(Things[thisT.contains[i].substring(1)].contains);
					}
					thisT.contains[i]="";
				}
			}
		}

		if (toConcat.length>0)
		{
			for (var i in toConcat)
			{
				thisT.contains.push(toConcat[i]);
			}
		}

		newContains=[];
		for (var i in thisT.contains)
		{
			if (thisT.contains[i]!="") newContains.push(thisT.contains[i]);
		}
		thisT.contains=newContains;

	}
    """
    pass


def __make(what):
    class Seed:
        def grow(seed_id):
            pass

        def list_seed():
            pass

    return Seed()


def start_nested():
    def __launch_nest(what="universe"):
        thing = __things.get(what)
        if thing is None:
            what = "error"

        seed = __make(what)
        seed.grow(0)
        seed.list()

    __clean_things()

    return __launch_nest()
