"""Name the Robot Band (make.fun bounty u-motasimfuad-name-the-robot-band-1ffc6a74).

Writes one funny robot band name plus a few words on its hit song to
/output/entry.txt (or $OUTPUT_DIR/entry.txt for local tests).

Candidates considered (each under 200 characters, judged head to head
on: funny on first read, hit song adds a second laugh, sounds like a
real band, no filler):

A. "The Rusty Bolts, a robot band that only plays power ballads.
   Hit single: 'I Will Always Lug You'." (97 chars)
   Decent pun, but "lug" is a weak second laugh and the name is generic.

B. "Ctrl+Alt+Defeat, a robot band that lost every battle of the bands.
   Hit single: 'Turn It Off and On Again'." (106 chars)
   WINNER. The name is a real joke on first read (Ctrl+Alt+Del turned
   into Defeat), "lost every battle of the bands" lands a second beat
   that fits the name, and the hit single is the classic tech-support
   line, a second laugh that fits a band of robots perfectly. It
   sounds like a band you would repeat to a friend, and it is tight
   at 106 characters with no filler.

C. "The 404s, a robot band with no hits and no homepage.
   Hit single: 'Feelings Not Found'." (86 chars)
   Clean and short, but "Feelings Not Found" is a thinner second laugh
   than B's hit single and "no homepage" adds little.

D. "The Roombas, a robot band that cleans up at every gig.
   Hit single: 'Bump Into the Wall'." (88 chars)
   "Cleans up at every gig" is good, but the hit song title has no
   punch of its own.

E. "The Tin Men, a robot band with no heart but perfect pitch.
   Hit single: 'Oil Be There for You'." (94 chars)
   Strong runner up: "Oil Be There for You" is a great pun. But
   "Tin Men" reads less instantly as a robot band than B, and the
   Wizard of Oz nod needs a beat to land.

F. "Beep Boop and the System Errors, a robot band that only plays
   weddings it crashed. Hit single: 'Have You Tried Turning Me Off
   and On Again'." (140 chars)
   Too wordy, the hit title repeats B's joke at twice the length,
   and the name is a mouthful.

How the winner was picked: the judge is a stand-up comic who has
heard every robot joke twice, so a pun-shaped noise loses to a real
joke. B wins because every part does work: the name is the joke
(Ctrl+Alt+Del becomes Defeat), the "battle of the bands" line is a
second joke that only works with that name, and the hit single is
the one line every robot owner has heard, which makes the band feel
real. Nothing in the entry explains the joke, and nothing is filler.
The other candidates each fail one of those tests: A and D have a
weak second laugh, C is thin, E needs a beat to land, F is bloated.
"""

import os

WINNER = (
    "Ctrl+Alt+Defeat, a robot band that lost every battle of the bands. "
    "Hit single: 'Turn It Off and On Again'."
)

MAX_CHARS = 200


def validate_length(text: str) -> None:
    """Raise if the entry would fail the gate (1 to 200 characters)."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1 to 200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")


def write_entry(text: str, output_dir: str) -> str:
    """Write text to entry.txt inside output_dir, return its path."""
    validate_length(text)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    write_entry(WINNER, output_dir)


if __name__ == "__main__":
    main()
