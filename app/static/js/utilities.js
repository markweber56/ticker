// set html header attributes
function setupHeader() {
	console.log("setup header function called");
	var navWidth = $("nav").css("width");
	navWidth = parseInt(navWidth);
	console.log("navbar width: ",navWidth);
	$(".endo-dd").css("right",navWidth/8);
};

// size upload buttons ("upload.html")
function sizeButtons(){
	
	div_width = $("#button-row").css("width");
	div_width = parseInt(div_width);
	console.log("jQuery div width: ",div_width);
	btn_width = Math.round(div_width/6);
	
	$(".btn-endo").css("width",btn_width);
	console.log("button width",btn_width);
	whiteSpace = div_width-2*btn_width;
	btn_spacer = Math.round(whiteSpace/12);
	console.log("spacer width",btn_spacer);
	$(".btn-left").css("right",btn_spacer);
	$(".btn-right").css("left",btn_spacer);
};

// setup reader characterization upload page
function setupUpload() {
	console.log("setup function called")
	$(".dropdown-toggle").dropdown();
	console.log("call setup header");
	setupHeader(); // set the navbar geometry
	
	console.log("attach event to buttons") // add events to buttons
	$('#buttonid').click(function(){
	$('#fileid').click();
	console.log("you clicked the fake button")
	});
	$('#submitButton').click(function(){;
		$('#formid').submit();
	});
	
	console.log("set button geometry");
	sizeButtons();
	console.log("endsetup");
};

// set "plotter.html" attributes
function setupPlotter() {
	console.log("setting up plotter");
	setupHeader();
	$(".dropdown-toggle").dropdown();
};

// adjust lines between data points
// subroutine of plotRaderData()
function shorten(p0,p1,r) {
	dx = xScale(p1[0])-xScale(p0[0]);
	dy = yScale(p1[1])-yScale(p0[1]);
	theta = Math.atan((dy/dx));
	xshift = (r*Math.cos(theta));
	yshift = (r*Math.sin(theta));
	// console.log('xshift: ',xshift);
	// console.log('yshift: ',yshift);
	if(p1[0]>=p0[0]) {
		arr = [p0[0],p1[0],p0[1],p1[1],xshift,yshift];
	} else { arr = [p1[0],p0[0],p1[1],p0[1],xshift,yshift] };
	return arr
	// return [p0[0],p1[0],p0[1],p1[1]];
};	

// get coordinates for drawing lines between data points
// subroutine of plotReaderData()
function lineCoords(dataset,r) {
	coords = [];
	for(var i=0; i<dataset.length-1; i++) {
		p0 = dataset[i];
		p1 = dataset[i+1];
		coords.push(shorten(p0,p1,r));
	};
	return coords;
};

// parse reader char / verification data by emulator value
function parseArray(dataset) {
	
	// get unique emulator values
	emArr = [dataset[0][2]];
	for(var i=0; i<dataset.length; i++) {
		val = dataset[i][2];
		inSet = 0;
		for(var p=0; p<emArr.length; p++) {
			if(val==emArr[p]) {
				inSet = 1;
			};
		}
		if (inSet==0) {
			emArr.push(val);
		};
	};
	// parse ss, freq data by emulator value
	parsed = new Array(emArr.length);
	for(var i=0; i<emArr.length; i++) {
		emVal = emArr[i];
		tempArr = [];
		for(var k=0; k<dataset.length; k++) {
			row = dataset[k];
			if(row[2] == emVal) {
				tempArr.push([row[0],row[1]]);
			};
		};
		parsed[i] = tempArr;
	};
	return parsed;
};

// get coordinates for drawing star around center coordinates
function starCoords(coords,r) {
	
	var pi = Math.PI;
	stars = new Array(coords.length); // contains coordinates x,y coordinates for n stars
	angles = [0,pi/4,pi/2,(3/4)*pi]; // rotational angle of star lines
	linCoords = new Array(4); // [x1,x2,y1,y2] for each line
	
	for (k=0; k<coords.length; k++) { // number of stars
		row = coords[k]; //x,y coordinates of star center
		// console.log('row: ',row);
		linCoords = new Array(4);
		
		for(i=0; i<angles.length; i++) { // three angles for 3 lines
			theta = angles[i];
			x1 = xScale(row[0])+r*Math.cos(theta);
			x2 = xScale(row[0])-r*Math.cos(theta);
			y1 = yScale(row[1])+r*Math.sin(theta);
			y2 = yScale(row[1])-r*Math.sin(theta);
			
			linCoords[i] = [x1,x2,y1,y2];
		};
		// console.log('linCoords: ',linCoords);
		stars[k] = linCoords;
	};
	return stars;
};

// generate svg graphic from reader characterization/ verification data
function plotReaderData() {
	var r = 5;
	var sw = 2; // stroke width
	
	var parsed = parseArray(dataset);
	
	var circles = svg.selectAll("circle")
		.data(dataset)
		.enter()
		.append("circle");
									
	var xAxis = d3.axisBottom()
					.scale(xScale)
					.tickFormat(d3.format("d"));
	
	var yAxis = d3.axisLeft()
					.scale(yScale);
					
	circles.attr("cx",function(d) {
				return xScale(d[0]);
			})
			.attr("cy",function(d) {
				return yScale(d[1]);
			})
			.attr("r",r)
			.attr("fill","none")
			.attr("stroke","black")
			.attr("stroke-width",sw);

	var dataset2 = parsed[0];
	// var data2 = lineCoords(dataset2,r);
	
	// var dataset2 = [[3400,12.9],[3800,13.2]];
	var data2 = lineCoords(dataset2,r+sw/2);
	
	// console.log('data2: ',data2);
	lines = svg.selectAll("line")
		.data(data2)	
		.enter()
		.append("line")
		.attr("x1",function(d) {
			return xScale(d[0])+d[4];
		})
		.attr("x2",function(d) {
			return xScale(d[1])-d[4];
		})
		.attr("y1",function(d) {
			return yScale(d[2])+d[5];
		})
		.attr("y2",function(d) {
			return yScale(d[3])-d[5];
		})
		.attr("stroke","black")
		.attr("stroke-width",3);
	
	for(var row=1; row<parsed.length; row++){
		dataset3 = parsed[row];
		// console.log("parsed data: ",dataset3)
		data3 = lineCoords(dataset3,r+sw/2);
		for(var i=0; i<data3.length; i++) {
			data2.push(data3[i]);
		};
		
		// var newLines = lines.data(data2).enter()
		var lines = svg.selectAll("line")
			.data(data2)
			
		lines.enter()
			.append("line")
			.attr("x1",function(d) {
			//	console.log("d: ",d);
				return xScale(d[0])+d[4];
			})
			.attr("x2",function(d) {
				return xScale(d[1])-d[4];
			})
			.attr("y1",function(d) {
				return yScale(d[2])+d[5];
			})
			.attr("y2",function(d) {
				return yScale(d[3])-d[5];
			})
			.attr("stroke","black")
			.attr("stroke-width",3)
			.merge(lines);
	};
	
	// parse failing data
	var failing = [];
	for(var i=0; i<dataset.length; i++) {
		row = dataset[i];
		if(row[3]==1.0) {
			console.log('failing');
			failing.push([row[0],row[1]]);
		};
	};
	
	var stars = starCoords(failing,r);
	
	var groups = svg.selectAll("g")
		.data(stars)
		.enter()
		.append("g")
			.selectAll("line")
			.data(function(d) {
				console.log(d);
				return d})
			.enter()
			.append("line")
			.attr("x1",function(d) {
			//	console.log(d)
				return d[0];
			})
			.attr("x2",function(d) {
				return d[1];
			})
			.attr("y1",function(d) {
				return d[2];
			})
			.attr("y2",function(d) {
				return d[3];
			})
			.attr("stroke","red")
			.attr("stroke-width",1);
			
	// create x axis
	svg.append("g")
		.attr("class","axis")
		.attr("transform","translate(0," + (h - padding) + ")")
		.call(xAxis);
		
	// create y axis
	svg.append("g")
		.attr("class","axis")
		.attr("transform","translate("+2*padding+",0)")
		.call(yAxis);
};

function gear(d) {
  var n = d.teeth,
      r2 = Math.abs(d.radius),
      r0 = r2 - 8,
      r1 = r2 + 8,
      r3 = d.ring ? (r3 = r0, r0 = r1, r1 = r3, r2 + 20) : 20,
      da = Math.PI / n,
      a0 = -Math.PI / 2 + (d.ring ? Math.PI / n : 0),
      i = -1,
      path = ["M", r0 * Math.cos(a0), ",", r0 * Math.sin(a0)];
  while (++i < n) path.push(
      "A", r0, ",", r0, " 0 0,1 ", r0 * Math.cos(a0 += da), ",", r0 * Math.sin(a0),
      "L", r2 * Math.cos(a0), ",", r2 * Math.sin(a0),
      "L", r1 * Math.cos(a0 += da / 3), ",", r1 * Math.sin(a0),
      "A", r1, ",", r1, " 0 0,1 ", r1 * Math.cos(a0 += da / 3), ",", r1 * Math.sin(a0),
      "L", r2 * Math.cos(a0 += da / 3), ",", r2 * Math.sin(a0),
      "L", r0 * Math.cos(a0), ",", r0 * Math.sin(a0));
  path.push("M0,", -r3, "A", r3, ",", r3, " 0 0,0 0,", r3, "A", r3, ",", r3, " 0 0,0 0,", -r3, "Z");
  return path.join("");
}