# Instructor Technical Setup

This guide will help you to get your laptop configured and able to run both the technical content of the Academy and the RevealJS presentations.

## How The Academy Resources work

All course content is located in named folders, i.e. `apis` `python-1` etc etc. Each taught module has a directory which contains a slide deck Markdown, as well as other supporting files such as exercises, solutions and handouts.

The taught content in this repository is written as Markdown for easy editing, and presented as nice slides in a web browser using [reveal-md](https://github.com/webpro/reveal-md), an NPM module derived from [revealjs](https://revealjs.com/) which allows for the creation of slide decks from markdown.

To ensure all academy have a common branding, styling and tools we have utilised [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to allow access to a common repo [academy-presentation-tooling](https://github.com/infinityworks/academy-presentation-tooling), from any curriculum/launchpad repo.

All module slide decks inherit a common `base.css` theme, which lives in the [./academy-presentation-tooling/static](./academy-presentation-tooling/static) directory. All academy programmes have access to extended themes such as 'schooloftech', 'ngeindia' etc etc , which allows for academy-specific branding.

The slides are converted into PDFs for distribution using the [decktape](https://github.com/astefanutti/decktape) NPM utility.

We use [MakeFile](https://www.gnu.org/software/make/manual/make.html) targets to simplify the commands to initialise installations, pull submodules, run presentations, convert presentations to pdf, zip folders, etc etc.

## Initial setup

You can either install Docker or Podman.

### Step 1. Install Docker:

You will need to get a valid WBS code and follow Accenture's process to authorise usage of Docker on your machine.

[https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

Note\* If unable to have access Docker there is a local way to run the presentations you can skip any specific `make dockerise` commands below

### Step 2. Install `Make`:

- **MacOS**

```sh
brew install make
```

- **WSL/Ubuntu**

```sh
sudo apt-get update
sudo apt-get install build-essential -y
```

For those on Windows we suggest using `WSL2` for everything, and checking out this repo in the WSL2 filesystem (not the linked windows folders via `/mnt/`).

If you wish to use Git Bash, you will need to do the following:

1. Open Git Bash as Administrator
1. Run the following command: `choco install zip make`

This will allow you to run almost all of the make commands, except `local-stop` because Git Bash does not have `lsof`.

Note: If you get an error due to script permissions, you can do the following:

1. Open PowerShell as Administrator
1. Run the following command: `Set-ExecutionPolicy RemoteSigned`

This will reduce your PowerShell security, so it is recommended this is reverted when possible with the following command: `Set-ExecutionPolicy Restricted`

### Step 3. Perform the installation commands

the below commands will install all required dependencies, pull git submodules (which includes all readme's, styling, MakeFiles, scripts, and docker image), create our docker image for us, and allows us to use RevealJS to produce and run our materials

```sh
`make install`           # Install the node prerequisites e.g. RevealJS and git hooks
`make dockerise-all`     # Build the base and data images so we can run Reveal later
```

Note\* The base docker image installed should be stable. But if the scripts or static resources inside academy-presentation-tooling directory change, you will need to run this command:

```sh
`make dockerise-data`    # Add scripts and static resources to the base image
```

## Next Steps

Once all above setup has been completed you will have have access to all shared readme's, make commands and tools inside our submodule [academy-presentation-tooling](./academy-presentation-tooling) repo.

Below are specific readmes for this Curriculum

- [README-02-curriculum-specific-technical-setup](./README-02-curriculum-specific-technical-setup.md) - Extra technical setup that is specific to this repos curriculum.
- [README-03-curriculum-specific-course-setup.md](./README-03-curriculum-specific-course-setup.md) - Non-technical course set up that is specific to this repos curriculum.

Then the following readmes inside the [academy-presentation-tooling](./academy-presentation-tooling/) directory talk you through how to use, run and modify the academy resources.

- [README-01-using-revealjs.md](./academy-presentation-tooling/README-01-using-revealjs.md) - How to run sessions.
- [README-02-makefile-cheatsheet.md](./academy-presentation-tooling/README-02-makefile-cheatsheet.md) - Common Make commands.
- [README-03-contributing-to-sessions.md](./academy-presentation-tooling/README-03-contributing-to-sessions.md) - How to contribute to resources.
- [README-our-philosophy.md](./academy-presentation-tooling/README-our-philosophy.md) - Academy's main philosophy.
