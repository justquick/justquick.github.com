(function() {
  var Mario, choose, randInt,
    __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  choose = function(choices) {
    return choices[Math.floor(Math.random() * choices.length)];
  };

  randInt = function(max, min) {
    if (min == null) {
      min = 0;
    }
    return Math.floor(Math.random() * (max - min + 1)) + min;
  };

  Mario = (function() {
    function Mario() {
      this.update = __bind(this.update, this);
      this.playerPlatform = __bind(this.playerPlatform, this);
      this.updatePlayer = __bind(this.updatePlayer, this);
      this.updateBaddies = __bind(this.updateBaddies, this);
      this.create = __bind(this.create, this);
      this.createPrizes = __bind(this.createPrizes, this);
      this.createPlayer = __bind(this.createPlayer, this);
      this.createPlatforms = __bind(this.createPlatforms, this);
      this.createBaddie = __bind(this.createBaddie, this);
      this.preload = __bind(this.preload, this);
      this.gameOver = __bind(this.gameOver, this);
      this.collectStar = __bind(this.collectStar, this);
      this.game = window.game = new Phaser.Game(800, 600, Phaser.AUTO, '', {
        preload: this.preload,
        create: this.create,
        update: this.update
      });
      this.score = 0;
      this.scoreText;
    }

    Mario.prototype.collectStar = function(player, star) {
      star.kill();
      this.score += 1;
      this.scoreText.text = 'Score: ' + this.score;
      if (this.score === 12) {
        this.scoreText.text = 'YOU WIN!';
        return this.game.paused = true;
      }
    };

    Mario.prototype.gameOver = function(player, baddie) {
      this.scoreText.text = 'GAME OVER!';
      return this.game.paused = true;
    };

    Mario.prototype.preload = function() {
      this.game.load.image('sky', 'assets/images/sky.png');
      this.game.load.image('grass', 'assets/images/grass.png');
      this.game.load.image('star', 'assets/images/star.png');
      this.game.load.image('rock', 'assets/images/rock.png');
      this.game.load.spritesheet('dude', 'assets/images/dude.png', 32, 48);
      this.game.load.spritesheet('baddie', 'assets/images/baddie.png', 32, 32);
      return this.cursors = this.game.input.keyboard.createCursorKeys();
    };

    Mario.prototype.createBaddie = function() {
      var baddie;
      baddie = this.baddies.create(randInt(800), 0, 'baddie');
      this.game.physics.arcade.enable(baddie);
      baddie.body.bounce.y = 0.0;
      baddie.body.gravity.y = 10000;
      baddie.body.collideWorldBounds = true;
      baddie.animations.add('left', [0, 1], 10, true);
      baddie.animations.add('right', [2, 3], 10, true);
      return baddie.direction = choose(['left', 'right']);
    };

    Mario.prototype.createPlatforms = function() {
      var h, rock, tile, w, _i, _j, _results;
      this.platforms = window.platforms = this.game.add.group();
      this.platforms.enableBody = true;
      this.tiles = window.tiles = {};
      _results = [];
      for (w = _i = 0; _i <= 16; w = ++_i) {
        for (h = _j = 1; _j <= 10; h = ++_j) {
          tile = this.platforms.create(w * 50, h * 50, 'grass');
          tile.body.immovable = true;
          tile.body.checkCollision.left = false;
          tile.body.checkCollision.down = false;
          tile.body.checkCollision.right = false;
          if (this.tiles[w] == null) {
            this.tiles[w] = {};
          }
          this.tiles[w][h] = tile;
        }
        rock = this.platforms.create(w * 50, 550, 'rock');
        _results.push(rock.body.immovable = true);
      }
      return _results;
    };

    Mario.prototype.createPlayer = function() {
      this.player = window.player = this.game.add.sprite(0, 0, 'dude');
      this.game.physics.arcade.enable(this.player);
      this.player.body.bounce.y = 0.2;
      this.player.body.gravity.y = 600;
      this.player.body.collideWorldBounds = true;
      this.player.animations.add('left', [0, 1, 2, 3], 10, true);
      return this.player.animations.add('right', [5, 6, 7, 8], 10, true);
    };

    Mario.prototype.createPrizes = function() {
      var i, star, _i, _results;
      this.stars = this.game.add.group();
      this.stars.enableBody = true;
      _results = [];
      for (i = _i = 0; _i <= 11; i = ++_i) {
        star = this.stars.create(randInt(800), randInt(550), 'star');
        star.body.gravity.y = 600;
        _results.push(star.body.bounce.y = 0.7 + Math.random() * 0.2);
      }
      return _results;
    };

    Mario.prototype.create = function() {
      this.game.add.sprite(0, 0, 'sky');
      this.scoreText = this.game.add.text(0, 0, 'Score: 0', {
        fontSize: '32px',
        fill: '#000'
      });
      this.createPlatforms();
      this.createPlayer();
      this.createPrizes();
      this.baddies = window.baddies = this.game.add.group();
      return this.game.time.events.repeat(Phaser.Timer.SECOND * 3, 10, this.createBaddie);
    };

    Mario.prototype.updateBaddies = function() {
      var baddie, _i, _j, _len, _ref, _results, _results1;
      _ref = this.baddies.children;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        baddie = _ref[_i];
        if (baddie.body.position.x === 0) {
          baddie.direction = 'right';
        } else if (baddie.body.position.x === 768) {
          baddie.direction = 'left';
        }
        if (baddie.direction === 'right') {
          baddie.body.velocity.x = randInt(200, 400);
          baddie.animations.play('right');
        } else {
          baddie.body.velocity.x = 0 - randInt(200, 400);
          baddie.animations.play('left');
        }
        if (choose((function() {
          _results1 = [];
          for (_j = 0; _j <= 30; _j++){ _results1.push(_j); }
          return _results1;
        }).apply(this)) === 10) {
          _results.push(baddie.body.velocity.y = -900);
        } else {
          _results.push(void 0);
        }
      }
      return _results;
    };

    Mario.prototype.updatePlayer = function() {
      this.player.body.velocity.x = 0;
      if (this.cursors.left.isDown) {
        this.player.body.velocity.x = -150;
        this.player.animations.play('left');
      } else if (this.cursors.right.isDown) {
        this.player.body.velocity.x = 150;
        this.player.animations.play('right');
      } else {
        this.player.animations.stop();
        this.player.frame = 4;
      }
      if (this.cursors.up.isDown && this.player.body.touching.down) {
        return this.player.body.velocity.y = -250;
      }
    };

    Mario.prototype.playerPlatform = function(player, platform) {
      if (this.cursors.down.isDown && this.player.body.touching.down) {
        platform.destroy();
        return platform.body.checkCollision.up = false;
      }
    };

    Mario.prototype.update = function() {
      this.game.physics.arcade.collide(this.player, this.platforms, this.playerPlatform);
      this.game.physics.arcade.collide(this.platforms, this.stars);
      this.game.physics.arcade.overlap(this.player, this.stars, this.collectStar);
      this.game.physics.arcade.collide(this.baddies, this.platforms);
      this.game.physics.arcade.collide(this.player, this.baddies, this.gameOver);
      this.updateBaddies();
      return this.updatePlayer();
    };

    return Mario;

  })();

  window.mario = new Mario;

}).call(this);
