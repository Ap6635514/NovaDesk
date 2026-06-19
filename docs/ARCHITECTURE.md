# NovaDesk Architecture

UI
↓

Components

↓

Pages

↓

Services

↓

Filesystem

Each layer has one responsibility.

UI never moves files.

Services never create widgets.

Filesystem never touches UI.