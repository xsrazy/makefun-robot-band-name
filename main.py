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
"""

import os

WINNER = (
    "Ctrl+Alt+Defeat, a robot band that lost every battle of the bands. "
    "Hit single: 'Turn It Off and On Again'."
)

MAX_CHARS = 200


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WINNER)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
