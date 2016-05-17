package  {
	
	import flash.display.MovieClip;
	
	public class CColleague extends MovieClip {

		public var dir_x;
		public var dir_y;
		
		public function CColleague() {
			// constructor code
			dir_x = Math.round(Math.random());
			dir_y = true; 
			
			this.y = 300 + 150*Math.random();
			this.x = 840*Math.random();
		}
		
		public function run(){
			
			if(this.x > 840) {	
				this.dir_x = false;
				this.y -= 30;
			}
			
			if(this.x < 0) {
				this.dir_x = true;
				this.y -= 30;
			}
			
			if(dir_x)
				this.x += 3;
			else 
				this.x -= 3;
			
			if(Math.round(this.x % 167) == 0){
				this.gotoAndStop( (this.currentFrame + 12*Math.round(Math.random()*4)) % 48 ); 
			}
		}
		
		public function getColleagueID(){
			var t = (this.currentFrame - 1) % 12;
			var c = "";
			
			switch(t){
				case 0: c = 'Catherine'; break;
				case 1: c = 'Bartozs'; break;
				case 2: c = 'Dale'; break;				
				case 3: c = 'Billy'; break;				
				case 4: c = 'Natalia'; break;
				case 5: c = 'Bally'; break;	
				case 6: c = 'Mayur'; break;
				case 7: c = 'Nick'; break;
				case 8: c = 'Richard'; break;
				case 9: c = 'Rodrigo'; break;
				case 10: c = 'Vipul'; break;
				case 11: c = 'Derek'; break;
			}
			
			return c;
		}
	}
	
}