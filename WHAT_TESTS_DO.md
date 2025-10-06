## What tests do

1. `tests.TestPublicPages`:
   Public, unauthenticated flows of your app: opening the landing page, navigating between Landing → Sign-up → Login, and handling a failed login. The setup_elements_for_test fixture likely injects page objects on the test class (self.landing_page, self.login_page, self.signup_page). Each test dismisses a cookie banner if it appears.
   
   - `test_landing_links_present`
     Intent: The landing page loads correctly and shows the key public UI (links/CTAs you expect on first load).
     Steps: Open landing → accept cookies → expect_loaded() (which likely asserts required elements are visible).

   - `test_navigate_to_login`
     Intent: A user can reach the Login screen via the Sign-up page (cross-navigation works).
     Steps: Open landing → accept cookies → go to Sign-up → from there go to Login → assert Login page loaded.

   - `test_navigate_to_signup`
     Intent: A user can reach the Sign-up page from the landing page.
     Steps: Open landing → accept cookies → go to Sign-up → assert Sign-up page loaded.

   - `test_login_negative_incorrect_creds`
     Intent: Invalid credentials are rejected with the correct error feedback.
     Steps: Open Login directly → accept cookies → assert page loaded → attempt login with bogus email/password → assert error message/state is shown.

2. `tests.TestFeedAuth`:
   Behavior of the Home feed for a signed-in user: that posts render, and that the user can like and save the first post shown.

   - `test_feed_shows_posts`
     Intent: The Home feed actually displays posts and the basic interaction UI is present.
     Steps:
        Navigate to the Home tab.
        Assert the feed is visible (expect_feed_visible() checks that an <article> is on-screen).
        Grab the first post (first_post).
        Scroll until the “liked by” area of that post is in view (ensures the card is fully interactable).
        Verify the comment button exists/visible on that post (sanity check that engagement controls are rendered).

   - `test_can_like_first_post`
     Intent: The user can like a post from the Home feed.
     Steps:
        Go to Home.
        Get the first post, scroll it fully into view.
        Confirm the comment button is visible (post is fully loaded/interactive).
        Perform the action: `first_post.like()`.
     Cleanup: `cleanup_unlike_first` undoes the like so future tests start clean.

   - `test_can_save_first_post`
     Intent: The user can save/bookmark a post from the Home feed.
     Steps:
        Go to Home.
        Get the first post, scroll it into view.
        Confirm the comment button is visible.
        Perform the action: `first_post.save()`.
     Cleanup: `cleanup_remove_first` removes the saved state afterward.
