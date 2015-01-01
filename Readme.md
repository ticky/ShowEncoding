# Show Encoding

Simple plugin for Sublime Text 2 to show the file encoding in the status bar.

## Compatibility

This plugin is only available for Sublime Text 2, as Sublime Text 3 has included this feature [since build 3059](http://www.sublimetext.com/3). Instructions to enable the Sublime Text 3 equivalent are available in [this Stack Overflow answer](http://stackoverflow.com/a/20657899/288906).

## Installation

You may either install using Package Control (which gains you automatic updates and a simpler install), or manually using `git`.

### Package Control (Recommended)

1. Install [Sublime Package Control](http://wbond.net/sublime_packages/package_control/installation).
2. Run `Package Control: Install Package` from the Command Palette
3. Find and install the `Show Encoding` plugin

### Manual

1. CD into your Sublime Text 2 Packages directory;
	* Windows: `%APPDATA%\Sublime Text 2\Packages\`
	* OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
	* Linux: `~/.config/sublime-text-2/Packages/`
	* Portable Installation: `Sublime Text 2/Data/Packages/`
2. `git clone https://github.com/grapegravity/ShowEncoding.git`

## Usage

A file's encoding will be displayed in the status bar. This is automatically updated on load and on save. There are no settings to configure.
